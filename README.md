# Running dev server
To develop - run `make dev` to get a development server with a reloader

# Running prod server
Press the run button, or `make prod`

## Run on dev mode
Add a new `micro`to your `Spacefile`:
```
  - name: devMode
    src: ./
    engine: python3.9
    dev: uvicorn main:app --reload --host 0.0.0.0
```
and don't forget to make your first `micro` as `primary: true`, then run:
```
space dev
```
You should see a link to open the app in dev mode.