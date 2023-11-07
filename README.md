# Event Booking System
The Event Booking System is a web application that allows users to explore and book tickets for both offline and online events. Users can also view their booked events and manage their account through secure login and logout functionalities. The project aims to provide a seamless event booking experience for users.

## Features
- Browse a list of offline and online events.
- Book tickets for selected events.
- View a personalized list of booked events.
- Secure user authentication with login and logout capabilities.

## Future Scope
- In the future, the project can be extended to include the following features:
- Integration of a payment gateway for convenient and secure online payments.
- Enhanced event recommendation algorithms.
- User reviews and ratings for events.
- Real-time notifications for event updates and booking confirmations.

## Technologies Used
The Event Booking System is built using the following technologies:
- Python
- Django
- Django REST Framework
- PostgreSQL (Database)
- Docker (Containerization)
- AWS (Amazon Web Services)
- Nginx (Web Server)

## Deployment
The project was deployed on AWS using Docker containers and Nginx for web server functionality, ensuring scalability and reliability.

### Step 1: Install and Configure Depdencies

Use the below commands to configure the EC2 virtual machine running Amazon Linux 2.

Install Git:

```sh
sudo yum install git -y
```

Install Docker, make it auto start and give `ec2-user` permissions to use it:

```sh
sudo yum install docker -y
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -aG docker ec2-user
```

Note: After running the above, you need to logout by typing `exit` and re-connect to the server in order for the permissions to come into effect.

Install Docker Compose:

```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```


### Step 2: Project Setup


#### Cloning Code

Use Git to clone your project: Navigate to `/home/ec2-user/`

```sh
git clone <project ssh url>
```

Note: Ensure you create an `.env` file before starting the service.

### Step 3: Running Service

To start the service, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml up -d
```



### Step 4: Update Server


 To update server with new changes, run:

```
git pull origin <branch name>
```

```sh
sudo docker restart app
```
---

To rebuild the container, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml build <container>
```

To apply the update, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml up --no-deps -d <container>
```

example:
```sh
sudo docker-compose -f docker-compose-deploy.yml up --no-deps -d app
```

The `--no-deps -d` ensures that the dependant services (such as `proxy`) do not restart.

---

## Additional Commands

### Docker
To start the container, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml up <container> -d
```

To stop the service, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml down
```

To stop the container, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml down <container>
```

To stop service and **remove all data**, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml down --volumes
```


#### Viewing Logs

To view container logs, run:

```sh
sudo docker-compose -f docker-compose-deploy.yml logs
```

Add the `-f` to the end of the command to follow the log output as they come in.

#### Execute Command in Container
To execute command inside the docker, run:
```sh
docker exec -it <container> /bin/bash
```
example : `docker exec -it app /bin/bash`
