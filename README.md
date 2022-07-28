# Receive action from monday.com

In monday.com, you can create custom actions for your board. A purpose of a custom action would be to trigger a process only doable by an API deployed somewhere in the cloud for example.


# Setup

## Setup in monday.com

When first of, you will need to create an app on monday.com
To do so, go to your interface, click on your icon in the bottom left corner, and click on "Developers"

Then you will be able to create an app, and access it. In the "Basic information", you will see the client id, client secret and signing secret. Keep in mind that you will need this **signing secret** for your code.

You can then create a feature (select "Integration" as Feature type and "Start from Scratch" as a template).

In your feature, you can go to the "Workflow blocks" and create a new "action".
In your feature, you can modify multiple parameters

- Name of the action
- Input fields: the fields you need from the thing that is going to trigger your API. **CAREFUL**: Some fields are not compatible with every action (for example "Column values"). If not compatible, you will just not see your action when trying to attach it to your board.
- Sentence: an automation in monday.com is composed with a trigger and a action. This sentence will be found when updating your board in the action part. 
- API configuration: the url of your API, needs to be deployed first
- Publishing settings: only useful if you want your action to be visible by anyone using monday.com

Once your action is done, you can add it to your board in an automation. For example, you can add a button column, then edit the settings of your button to call the action you just created. Click on "More option" if you cannot find your action at first glance, custom actions are generally at the end of the list. 

**FYI:** you app does not need to be published or installed to see the action, you will need to publish it only if you want other users of your board to use it. A "Draft" app can be use on your personnal account.

## Setup in the code
The only thing you will need to do is create a `config.py` file by copying the `config_template.py`, and adding the *signing secret* we talked about earlier. You can find it in the "Basic information" tab of your app. Then simply install the requirements (or deploy your app), and add the link of your API to your action.
Then create a virtualenv with `python3 -m venv venv` and install dependancies with `pip install -r requirements.txt`, and you are good to go.