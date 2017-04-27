# Datapi
Datapi is a multithreaded fuzzing libary.
It is designed to work with RESTful API's
As well as crawl over html and spider through links, fields and buttons

At this time it is incomplete.


## datapi.py
simple  single page webscraper using beutiful soup. with little effort it can be added to a crawler to scrape every page of a website.


## replicant.py
a multithreaded concurrent network traffic generator. can send as little as 2 to as many as 20,000 connections per seccond. meant to test performance of a page. can also be used in conjuction with the fuzzer.py and datapi.py to replicate people using the site per seccond.


## fuzzer.py [Incomplete]
a fuzzing library for passive fuzzing using fusil and active simulated user experiences using Selenium


## program.py [incomplete]
location of the future program that will use all of these. this will come in the form of a CLI tool


