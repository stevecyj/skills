# Java Web Framework

A small synchronous HTTP framework for Java 17 or later. It uses the JDK `jdk.httpserver` module and has no runtime dependencies.

## Quick start

From the repository root, build the JAR and open JShell:

```sh
mvn -q -DskipTests -f java-web-framework/pom.xml package
jshell --class-path java-web-framework/target/java-web-framework-0.1.0.jar
```

At the `jshell>` prompt, enter:

```java
import io.github.stevecyj.webframework.*;
var app = new WebApplication();
app.route("GET", "/", request -> Response.text(200, "Hello, world!"));
app.start(8080);
```

In another terminal:

```sh
curl http://127.0.0.1:8080/
# Hello, world!
```

Stop the server in JShell with `app.stop();`, then enter `/exit`.

## Routes

```java
app.route("GET", "/hello/{name}", request ->
        Response.text(200, "Hello, " + request.pathParameter("name").orElseThrow()));
```

Register routes before calling `start`. Route patterns support literal segments and `{name}` parameters. More specific literal routes take precedence; ties use registration order. A missing path returns 404, a matching path with another method returns 405 with `Allow`, and an uncaught handler exception returns 500.

Run tests with `mvn test` from this directory.
