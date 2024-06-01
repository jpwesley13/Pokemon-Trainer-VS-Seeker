# Pokemon Trainer VS Seeker

The VS Seeker is an application with the primary function of allowing a Pokemon Trainer (henceforth "user") to register and reference rivals battled through a user's adventure. Though this is its primary function, the VS Seeker can also be used simply as a way to log and record trainers, or as a way for the user to keep track of their own progress. The VS Seeker allows the user to choose from a list of its registered trainers, offering them a selection of options for both the trainers and their known Pokemon.

## Initialization

When the VS Seeker is booted, the user is met with the simple options of viewing its registered trainers or shutting down the application. As the user progresses through their options they are given additional selections and access to additional features.

## Features

* User may view a list of all trainers they have registered to the VS Seeker.
* When viewing all registered trainers, the user may see additional details on any individual trainer, as well as register a new trainer to the VS Seeker.
* The user can update registered trainers' information including their name, badges, and Pokemon possessed. Additionally the user can remove the trainer from the VS Seeker.
* In addition to being able to register trainers, the user can create entries for new Pokemon a trainer possesses, as well as viewing the details of an individual Pokemon.
* Pokemon details can be updated by the user when viewing them, addressing increased level, new evolution, and other information.
* Simple menu navigation allows the user to return to their previous menus at any time or shut down the VS Seeker with ease.

## All Trainers

On the VS Seeker's second menu after entry, the user is presented with a list of all currently registered trainers. The trainers are numbered by order of registration, and the user may see additional details about any individual trainer by entering their respective number. On this menu the user may also register a new trainer.

## Register New Trainer

When the user wishes to register a new trainer to their VS Seeker, they are asked to enter that user's name, hometown, and current number of badges owned. The former two are entered as strings and the lattermost is entered as an integer between 0 and 8. If the user enters a value that does not conform to these constraints they will be met with an error message and the trainer will not be registered.

## Trainer Details

Upon selecting a trainer from the All Trainers menu, the user is met with a blurb of information on the trainer such as their name, hometown, and current counts of badges and Pokemon. Additionally all known Pokemon owned by that trainer are listed numerically in a similar format to the All Trainers menu.

On an individual trainer's details page, the user may update that trainer's information, in the event that they have undergone a name change or had a change in their badge count. The user is unable to change a trainer's hometown once they have been registered. Should the user no longer wish to keep track of this trainer, they may also remove the user and all associated Pokemon from their VS Seeker from this menu.

After registration or as new information is obtained, the user is able to add additional Pokemon to the trainer on their details page. When adding newly obtained Pokemon to a trainer, the user is asked to enter the Pokemon's nickname, its species, and its current level. After doing so the Pokemon will automatically be added to the list of Pokemon owned by that trainer. Like with the All Trainers menu, if the user enters a Pokemon's respective number on the list shown, they can explore additional details for it.

## Pokemon Details

When a Pokemon is selected from a trainer's details page, the user is met with a blurb telling them that the trainer has caught the associated Pokemon, detailing its nickname, species, and current level. From here the user is met with a menu where they may update that Pokemon's information.

Should a user wish to update a trainer's Pokemon, they will be asked what the Pokemon's new nickname is, what its new species is if it has evolved, and what its new level is. 

In addition to being able to update a Pokemon's information, the user may also remove the Pokemon from the trainer from the details page if its has been learned that it was released back into the wild.

## Menu Navigation

Menus on the VS Seeker are kept simple. The user is presented with clear instructions for each menu and prompting. Options are associated with sensible inputs that are case insensitive and the user is never required to enter more than one input when selecting a menu option. On all menu levels the user may return to the previous level with the universal "B" `back` input, as well as shut down the VS Seeker entirely with the universal "E" `exit` input.