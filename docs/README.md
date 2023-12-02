# A_Needle_in_a_Haystack_for_Python

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/a_needle_in_a_haystack_for_python/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_a_needle_in_a_haystack_for_python&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_a_needle_in_a_haystack_for_python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_a_needle_in_a_haystack_for_python&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_a_needle_in_a_haystack_for_python)
[![Build Status](https://github.com/gotreasa/a_needle_in_a_haystack_for_python/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/a_needle_in_a_haystack_for_python/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/a_needle_in_a_haystack_for_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/a_needle_in_a_haystack_for_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

Can you find the needle in the haystack?

Write a function `findNeedle()` that takes an `array` full of junk but contains one `"needle"`

After your function finds the needle it should return a message (as a string) that says:

`"found the needle at position "` plus the index it found the needle, so:

Example(Input --> Output)

```
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
```
