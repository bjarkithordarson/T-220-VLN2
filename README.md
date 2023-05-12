# T-220-VLN2
Verklegt námskeið 2 - Vor 2023 - Háskólinn í Reykjavík

## Getting started
### Virtual environment 
#### First setup
Setup the virtual environment. You only need to do this once. Do this in the project directory.
```
cd /path/to/project
python -m venv venv
```

#### Activate
Activate the virtual environment. You need to do this every time you start writing code:
#### Mac/Linux
```
source /path/to/project/venv/bin/activate
```

##### Windows
```
/path/to/project/venv/scripts/activate.bat
```

### Install
```
cd /path/to/project
pip install -r requirements.txt
```

### Starting the server
Run the commands:
```
cd pizzalair
python manage.py runserver --insecure
```

Open http://localhost:8000


## Test Users
| Username | Password | Notes |
| --- | --- | --- |
| admin | admin | Superuser. Has access to /admin. |
| Robert | mediumhardpassword | Has 10000 amount of loyalty points |
| Hall | realeasypassword | Has 1000 amount of loyalty points |
| Enrique | realyhardpassword | Has 250 amount of loyalty points |
| PizzaLover67 | ilovepizza67 | Has 13500 amount of loyalty points |
| FeedmePizza | PizzaIsMylife420 | Has 6900 amount of loyalty points |
| Dade | vinna1234 | Has 5500 amount of loyalty points |

## Functionality
### Requirements
| Requirement | Notes |
| --- | --- |
| Layout page | The layout was written from scratch by us. |
| Edit profile | /users/profile |
| Product catalouge | /products/pizza, /products/offers, /products/merch, /products/<category_slug> |
| Shopping cart | /cart |
| Product details | Products have a long description, more images (pizzas have a crust inspector) and a title |
| Buy a product - Contact | We called it billing info. Get to it by putting an item in your cart and clicking checkout. |
| Buy a product - Payment Step | Fully implemented |
| Buy a product - Review Step | Fully implemented |
| Buy a product - Confirmation step | Fully implemented |
| Buy a product - Navigation between steps | Fully implemented |
| Additional requirements | See next chapter. |
| PostgreSQL | In the cloud. |
| Model API | We made full use of Django's model API. |
| MTV pattern | We followed the MTV paradigm. |
| Git | Github was used as a repository. | 
| Exception handling | Data validation is handled through the models. No validation is made client-side without corresponding server-side validation. |
| Offer site | /products/offers |

### Additional functionality
#### Loyalty Points
Users earn loyalty points when orders are made. Certain products (merch) can only be bought using Loyalty Points.
#### Merch
Bought using Pizza Lair's own LP currency.
#### Crust Inspector
Pizza crusts can be inspected by hovering over the pizza picture. Crust lovers rejoyce!
#### Fully customizable offers
Offers are fully customizable. An offer consists of an Offer object, which has one or more OfferTemplates. When an offer is added to the cart, an OfferInstance is created according to the OfferTemplates specified in the Offer. An offer is added to the cart via a CartOfferItem.
#### CSS written by us
We took the chance to deepen our CSS knowledge by struggling through *so many* flex boxes. It may not be the most optimal CSS, but we love the final product and the experience it gave us.
#### Fully implemented admin site
The content is fully customizable through the admin site at /admin.
#### Super adorable 404 and 500 error pages
Just look at it :3

## If we had more time
### No JavaScript
There is partially (50-ish %) implemented functionality to make the whole website work without JavaScript.
### Deployment
We thought about deploying the app for fun. We might. The lair.pizza domain is available by the way ;)

## Stats
* Cups of coffees: 40
* Cans of monster: 15
* Pizzas eaten: 2
* Reports written: 2
* Hours worked: 150
* Merge conflicts: Too many
* Lost progress: Some
* Number of AI-generated dragon images: All of them.

## Links
* [OneDrive](https://reykjavikuniversity-my.sharepoint.com/:f:/r/personal/bjarkit22_ru_is/Documents/T-220-VLN2?csf=1&web=1&e=mCPupA)
* [Discord](https://discord.com/channels/1099577819748638780/1099587766150508687)
* [Canvas Course](https://reykjavik.instructure.com/courses/6838) ([Modules](https://reykjavik.instructure.com/courses/6838/modules), [Assignments](https://reykjavik.instructure.com/courses/6838/assignments))
