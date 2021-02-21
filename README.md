# TwistedEuclideanTSP
_Non-spanning version of the Euclidean Travelling Salesman Problem with a twist (shaken, not stirred)_

## Problem description
Bob is an independent contractor hired by AcmeExpress.
Every morning he gets a list of events - pickups and deliveries for the day.
He needs to choose which events he wants to do,
and he needs to do it as quickly as possible - before others claim the events.

AcmeExpress refunds their contractors for kms driven,
and pay based on number of packages delivered or picked up.

Bob likes driving, so he doesn't mind having very long days -
but he absolutely hates pickups
(deliveries can be left at the door,
but if the person isn't home for a pickup, that's a trip wasted).
He therefore limits himself to handling only one pickup per day.

To get paid the most,
Bob therefore picks as many deliveries as fits in his vehicle,
plus one pickup,
with a trip that's as long as necessary (though shorter is of course better).

## Input
The input is a CSV (semicolon as separator) and the following columns
- OrderNumber: a **positive** integer serving as a **unique** identifier
- X: x-coordinate
- Y: y-coordinate
- Volume: a **positive** integer, the capacity required for the event
- Type: type of event, either **'D'** for delivery or **'P'** for pickup.

## Running the code
Mark the src folder as the source root
(otherwise you might have to change some of the _using_ statements).

Run `__init__.py` with TwistedEuclideanTSP as the working directory.

Alternatively, run the different tests (with the tests as the working directory).