# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [9.0.1.3.3] - 2017-12-08
### changed
- Applies validation of dispenser only in pickings outgoing.

## [9.0.1.3.2] - 2017-11-17
### changed
- Adds restriction to dispenser to can only validate its own pickings.

## [1.3.1] - 2017-11-14
### changed
- Adds security over model stock.dispenser.
- Adds translate of new terms in es_MX.

## [1.3.0] - 2017-11-13
### added
- Filter "My orders by deliver" for dispensers and Group By "Dispenser" for stock managers.

## [1.2.0] - 2017-11-12
### changed
- Adds model stock.dispenser inheriting from model res.users.
- Adds views for configure stock dispensers.
- Adds button for activation/inactivation of dispensers.

## [1.1.0] - 2017-08-30
### added
- Adds field stock_picking_ids to the model res.users, this field allows get the pickings asociated to warehouse dispensers.

## [1.0.0] - 2017-08-30
### added
- Adds "Dispenser" field to document of stock picking. Assuming that the
  dispenser can be a user in Inventory / User group. This field can only be
  edited by the users in Inventory / Manager group.
