<div align="center">
  <h1>⚡️ DDD Course Platform Pet Project ⚡️</h1>
</div>

<p align="center">
  <a href="#requirements">Requirements</a>&nbsp;&nbsp;•&nbsp;
  <a href="#use">Set up the Project</a>&nbsp;&nbsp;•&nbsp;
  <a href="#postgres">PostgresSQL</a>&nbsp;&nbsp;•&nbsp;
  <a href="#rabbitmq">RabbitMQ</a>
</p>

<a name=requirements></a>
## Requirements

The project runs with [Python 3.12](https://www.python.org/downloads/release/python-3120/). 

The recommended way to install Python is using [pyenv](https://github.com/pyenv/pyenv) if you are on Linux or MacOS. Here is a summary of the steps,
but it's recommended to visit the documentation for more details.

<details><summary>Install Python with pyenv</summary>

1. Install pyenv:
    ```bash
    curl https://pyenv.run | bash
    ```

2. Set you bash profile to load pyenv. In my case I use fish:

    ```bash
    set -Ux PYENV_ROOT $HOME/.pyenv
    fish_add_path $PYENV_ROOT/bin
   ```
   
    Then, add the following line to `~/.config/fish/config.fish`:

    ```bash
    echo pyenv init - | source >> ~/.config/fish/config.fish
    ```
3. Install the selected Python version (you can see available version with `pyenv install --list`):
    ```bash
    pyenv install 3.12
    ```
4. Go to your project folder and select this Python version for the folder
    ```bash
    pyenv local 3.12
    ```
</details>

After installing _pyenv_ you only need to install the package manager, in this case I prefer
to use [pdm](https://github.com/pdm-project/pdm). Just need to run the following command on
your project folder:
    
```bash
pip install pdm
```

To install directly all dependencies, run:

```bash
make install
```

<a name=use></a>
## Set up the Project

In order to set up the project, you need to follow the steps below:

1. Clone the repository on you local machine
    ```bash
   git clone <repo_url>
   ```
2. Run the `make local-setup` command to be able to run the hooks inside [hooks](./scripts/hooks) folder.

> [!NOTE]
> If you want to ignore the hooks folder, you can remove it and just run `make install` command.

3. Run infra containers declared in the [docker-compose.yml](./docker-compose.yml) file:
    ```bash
    docker-compose up -d
    ```
4. Run the tests to check if everything is working:
    ```bash
    make test
    ```

<a name=postgres></a>
## PostgresSQL

@TODO 

<a name=event-sourcing></a>
## RabbitMQ

<details><summary>Python tutorial</summary>

- [`Producers`](#producers) publish messages to [`exchanges`](#exchanges).
- The [`exchanges`](#exchanges) takes those messages and route them to [`queues`](#queues).
- [`Exchanges`](#exchanges) distribute the messages to the [`queues`](#queues) based on the [`bindings`](#bindings).
- The [`consumers`](#consumers) are subscribed to [`queues`](#queues) and consume the messages from them.

<a name=exchanges></a>
### Exchanges

> They are responsible for getting [`producers`](#producers) messages and routing them to the [`queues`](#queues).

Exchanges can be configured with different attributes:

- `exchange`: The name of the exchange. If not set, a random exchange name will be generated.
- `durable`: If set to `True` the exchange will survive server restarts, otherwise it will be deleted.
- `auto_doelete`: If set to `True` the exchange will be deleted when no queues are bound to it.
- `exchange_type`: The type of the exchange. The default is `direct`, but there are other types like `fanout`, `topic`.
    - `'direct'`: The message is routed to the queues whose binding key exactly matches the routing key of the message.
    - `'fanout'`: The message is routed to all the queues bound to the exchange. Here routing key is ignored.
    - `'topic'`: The message is routed to the queues whose binding key matches the routing key of the message.

To create a new exchange we need to run the following command:

```python
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange="videos",
    exchange_type="topic"
)
```

<a name=queues></a>
### Queues

> They store messages until they are consumed by the [`consumers`](#consumers).

Queues can be configured with different attributes:
- `queue`: The name of the queue. If not set, a random queue name will be generated.
- `durable`: If set to `True` the queue will survive server restarts, otherwise it will be deleted.
- `exclusive`: If set to `True` the queue will be used by only one connection and will be deleted when the connection closes.
- `auto_delete`: If set to `True` the queue will be deleted when no consumers are connected to it.

To create a new queue we need to run the following command:

```python
channel.queue_declare(
    queue="users.send_email_on_video_created",
    durable=True,
    exclusive=True
)
```

> Creating queues are idempotent operations, so we can run the same command multiple times without any side effects.
> If we don't know who will create the queue first, we can create it in the [`producer`](#producers) and [`consumer`](#consumers) code.

<a name=bindings></a>
### Bindings

> They are the link between the [`exchanges`](#exchanges) and the [`queues`](#queues).

To let the [`exchange`](#exchanges) know where to send the messages we need to create a [`binding`](#bindings) between the [`exchange`](#exchanges) 
and the [`queues`](#queues).

```python
channel.queue_bind(
    exchange="videos",
    queue="users.send_email_on_video_created",
    routing_key="videos.created"
)
```

The [`queue`](#queues) will receive the messages when its `routing_key` matches the `binding_key` of the [`exchange`](#exchanges).

<a name=producers></a>
### Producers

> They are the services that publish messages to the [`exchanges`](#exchanges).

Producers are intended to be long-lived and open their connections on startup.

To publish an event we need to create an [`exchange`](#exchanges), we can't send a message directly to a [`queue`](#queues).
1. Declare the [`exchange`](#exchanges) they want to publish the message to (same steps as in the [exchanges](#exchanges) section):
    
    ```python
    channel.exchange_declare(
        exchange="videos",
        exchange_type="topic"
    )
    ```

2. Publish the message specifying the `exchange`(name) and the `routing_key` arguments if it's declared of type `topic` or `direct`. This
routing key should have the same name as the [`binding_key`](#bindings) of the [`queue`](#queues) that will receive the message.

    ```python
    channel.basic_publish(
        exchange="videos",
        routing_key="videos.created",
        body="Video Created!"
    )
    ```

    If we want to ensure that the event survives a server restart, we need to set the `delivery_mode` to `Persistent`:
    
    ```python
    import pika
    
    channel.basic_publish(
        exchange="videos",
        routing_key="videos.created",
        body="Video Created!",
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )
    ```

<a name=consumers></a>
### Consumers

> They are the services that consume the messages from the [`queues`](#queues).

Consumers are intended to be long-lived and open their connections on startup. We will say that a consumer is subscribed to a queue
when it starts consuming messages from it.

All consumers need to:
1. Define the [`queue`](#queues) they want to consume messages from. Additionally, they can define the [`exchange`](#exchanges) 
the queue will be subscribed to. As creating a [`queue`](#queues), this is an idempotent operation, so we will create just one exchange.

    ```python
    channel.exchange_declare(
        exchange="videos",
        exchange_type="topic"
    )
    channel.queue_declare(
        queue="users.send_email_on_video_created",
        durable=True,
        exclusive=True
    )
    ```

2. [Bind](#bindings) that [`queue`](#queues) to the [`exchange`](#exchanges) with the `routing_key`.

    ```python
    channel.queue_bind(
        exchange="videos",
        queue="users.send_email_on_video_created",
        routing_key="videos.created"
    )
    ```
   
3. Define a callback function that will be called when a message is received. This function will be responsible for
processing the message.

    ```python
    from pika.channel import Channel
    from pika.spec import BasicProperties, Basic
    
    def callback(channel: Channel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
        print(f"[x] Received {method.routing_key}: {body.decode()}")
    ```
   
    To ensure that the message is not lost if the consumer crashes it's recommended to add a manual message acknowledgment in the callback:
        
    ```python
    from pika.channel import Channel
    from pika.spec import BasicProperties, Basic
   
    def callback(channel: Channel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
        print(f"[x] Received {method.routing_key}: {body.decode()}")
        channel.basic_ack(delivery_tag=method.delivery_tag)
    ```

4. Start consuming messages by subscribing to the queue.

    ```python
    channel.basic_consume(
        queue="users.send_email_on_video_created",
        on_message_callback=callback,
        auto_ack=False  # Set to True if you want to automatically acknowledge the message
    )
    channel.start_consuming()
    ```
   
    When consuming, we can configure the [`queue`](#queues) to not send a new message to the consumer until it has processed and
    acknowledged the previous one. This is called _fair dispatch_ and can be set as follows:
    
    ```python
    channel.basic_qos(prefetch_count=1)
    ```
</details>

<details><summary>How is applied in the project</summary>

</details>