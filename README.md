[![CircleCI](https://circleci.com/gh/adityafarizki/bmi-calc.svg?style=svg)](https://app.circleci.com/pipelines/github/adityafarizki/bmi-calc?invite=true)

# BMI Calculator APP
To use this app you can go to https://bmi-calc-hf.herokuapp.com/?weight=your_weight_in_kg&height=your_height_in_metre


## CI/CD
The CI/CD process utilizes CircleCI as the main tool. You can click on the CircleCI badge to get invitation to see the project.

## Logging and Monitoring
This project uses Scalyr as the logging and monitoring tool. If you want to see the logging data, then you can contact me at adityafarizki@live.com.

## How To Run The Code
1. pull the repository
2. make sure you have python3 version >= 3.8.0 installed in your system
3. install poetry using the command `pip3 install poetry`
4. go to the project folder and initiate poetry shell using `poetry shell` command
5. run `poetry install` command to install all dependency
6. give execution permission to run script in the scripts folder `chmod +x scripts/start_prod.sh`
7. run the run script from the project root folder as such `./scripts/start_prod.sh`
8. if you want to run the test suite, execute this command `behave`
