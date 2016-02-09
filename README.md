#Description
Logic land.
- This is the repository for the web application, Logic Land.

#Database migration

App/Models (make migration) => DB/Tables (sqlmigrate) => App/dbsqlite (migrate)

#TODO List

- [X] Create Admin users
- [ ] Add more views
- [ ] Get some HTML
- [ ] Add front-end framework(Bootstrap, UIkit, ect...) UIkit looks pretty good if we want to learn something new.
- [ ] Import ThreeJS files
- [ ] Get a basic ThreeJS view
- [ ] Create models for logic-gates
- [ ] Shared folder for computation
- [ ] Add unit tests/specs
- [ ] Use CI for automated testing

#Rules for Contribution

- Everytime we make change, make it in a different branch in a PR
  - For every change in functionality, add tests.
  - Make sure that the tests pass in CI.
  - Other person reviews a PR and merges it.

- For new functionality, follow Behavior Driven Development.

- For an update in the code, follow Test Driven Development.

- If we make any database changes (adding new models, migration, adding superusers)
  - name the branch with "db_" perfix.
  - For testing this branch, create a new branch and delete it after testing.

- Append a 'comma' and 'new line' at the end of a hash/list/array.




