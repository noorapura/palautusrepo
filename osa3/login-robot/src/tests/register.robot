*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  noora  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  heiolen9kirjainta
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ö  heiolen9kirjainta
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ö1234  moisalasana6767
    Output Should Contain  username must include only letters

Register With Valid Username And Too Short Password
    Input Credentials  norpsukka  ii67
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  nooraeve  Pitkäsalasana6767
    Output Should Contain  New user registered

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command


