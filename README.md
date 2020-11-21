# Web Benchmarks

This repository contains code that I created to run simple tests on web frameworks that I would like to test
and collect information. When I see fit, I'll add more information here.

**IMPORTANT**: I know the code is not nice at the moment, no dependency injection, organization is a mess and you can
name a lot more! I just do not care at this stage! Perhaps I'll make it nicer in the future.

## Apps

I'll try different frameworks and languages, the expected endpoints on them are:

- `/api/live` : 200 to say everything is fine
- `/api/db-call` : Emulates a DB call
- `/api/calculation` : Creates an array and sorts it
- `/api/complete` : Emulates DB calls and some calculations
