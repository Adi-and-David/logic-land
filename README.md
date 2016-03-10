#Description
Logic land.
- This is the repository for the web application, Logic Land.

#Database migration

App/Models (make migration) => DB/Tables (sqlmigrate) => App/dbsqlite (migrate)

#TODO List

- [X] Create Admin users
- [ ] Add more views
- [ ] Get some HTML
- [ ] Add unit tests/specs (Black Box Testing)
- [ ] Add custom authentication
- [X] Figure out if users table/model could be edited in a migration.
  - [X] Understanding how the authentication/authorization stuff works in Django.
  - [ ] HTTP Basic Auth.
- [X] Reorganize directory structure acc to Django convention.
- [X] Add front-end framework(Bootstrap, UIkit, ect...) UIkit looks pretty good if we want to learn something new.
- [X] Import ThreeJS files
- [ ] Get a basic ThreeJS view
- [ ] Create models for logic-gates
  - [ ] Back-end
  - [ ] Front-end
- [ ] Shared folder for computation
- [ ] Distribute work across js and python to optimize efficiency
- [ ] Add unit tests
- [ ] Make Developer's guide
- [X] Use CI for automated testing
- [ ] Concurrency/Parallelism
- [ ] Hosting options
  - [X] Travis
  - [ ] Azure
- [ ] Load balancing

#Rules for Contribution

- Everytime we make change, make it in a different branch in a PR
  - For every change in functionality, add tests.
  - Make sure that the tests pass in CI.
  - Other person reviews a PR and merges it.

- For new functionality, follow Behavior Driven Development.

- For an update in the code, follow Test Driven Development.

- If we make any database changes (adding new models, migration, adding superusers)
  - add the label "db"
  - For testing this branch, create a new branch and delete it after testing.

- Append a 'comma' and 'new line' at the end of a hash/list/array.

- If you start working on something, just open a PR with wip.
