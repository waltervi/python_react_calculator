# Coding Challenge Backend 

## Pending things that I have not done

### Configuration files
I did not add any configuration files, all configuration is STATIC, in code (something BAD!).
Configuration should have been added (arguably) at least for:
* pagination : default page size
* default user balance
* URL to get random strings
* database configuration

### Pagination of queries
I added the idea of pagination for just one query in RecordDAO, but it is not used since pagination in 
this case is managed by the DataTable React component in the client.
This should have been implemented properly for other types of clients anyway.

### Default Balance
Again, default balance when a user is created is hardcoded, and this should be handled differently.
Maybe there is a business requirement for this, or at least be set in a configuration file.

### Logging and errors
I did not add logging to the project, for time reason mostly.
I also like adding and ID to every http request, so that ID is logged in the logs. 
This way you can track a whole complete request in the log file, otherwise you won't be able 
to follow it with multiple threads running, and If an error happens that ID is being returned to the client
to be able to follow errors in the logs.


## Libraries and technologies

### Serverless Framework
The only serverless framework I used with python is Zappa (https://github.com/zappa/Zappa)
And this involves creating an AWS account, creating users, generating secrets and keys, creating some AWS bucket for configuration files, and using the AWS CLI locally. 
I will need more time to test everything works for a proper presentation and this is a coding challenge, and I need more incentive to spend my time doing it.

So I will use the Flask Framework to do a presentation locally.

### Use of AWS technologies
Like I mentioned before, developing the project as serverless would imply this.
I would also have implied to use DynamoDb as database.

I will use the Flask framework, that is something I used before.

### Use of Vue.js
I know basics of Vue, I like it, but in order to use it I would have to study and investigate it. Until now I did not work in any company using Vue in order to learn it.

ReactJS will be used, without NextJS.

### Flask
I've only used Flask framework since I started with Python. I like it more than Django in terms that is lighter from almost any point of view, I personally don't like the restrictions of some frameworks that end up many times restricting the way to code and makes you fully dependent on them (This happened to me in the past working with other technologies and it is not something nice when things get difficult)

#### Security
No security protocols will be used, since I will use the default development server, and the project is more a demo than a production ready project.

Here, I could have used -> https://github.com/GoogleCloudPlatform/flask-talisman, and of course implement whatever security the 

Nevertheless, the session Cookie will be checked on every API call.


### Session Management and Authentication
I will use the default session management that comes with Flask. This idea won't work with an application with thousands of user's. In that case I would suggest other techniques for session management, like saving a user_token in a centralized database.
This would allow to scale servers horizontally (with AWS Elastic Beans Talk for example) or proper use of serverless frameworks (like Zappa), since servers or apis can scale horizontally while the authentication is done in one server.

#### Authorization and permissions
Only authentication checks will be done, checking for a valid session cookie on every request.

#### Database
In order to not include more complexity and configuration I will go for the default SQLite.


## Install and run 

###  clone the repository
    $ git clone git@github.com:waltervi/truenorth_cd_backend.git
    $ cd truenorth_cd_backend

### Create a virtualenv and activate it::

    $ python3 -m venv .venv
    $ . .venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv .venv
    $ .venv\Scripts\activate.bat

### Install Flaskr::

    $ pip install -e .

Or if you are using the main branch, install Flask from source before installing Flaskr::

    $ pip install -e ../..
    $ pip install -e .


### Run the API Server

#### Initialize the database
    $ flask --app app init-db    

#### Run the project
    $ flask --app app run --debug

    This will run the api server in port 5000

### Tests
#### Install dependencies
    $ pip install pytest coverage

#### Run tests
    $ python -m pytest

#### Run with coverage report::
    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser



