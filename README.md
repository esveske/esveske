# esveske - main repository

## Setup

Clone this repository and `cd` into it.

```sh
git clone https://github.com/esveske/esveske
cd esveske
```

Clone the site into `gen/` directory:

```sh
git clone https://github.com/esveske/esveske.github.io gen
```

## Building

Just run `make`. It should rebuild everything.

Since you probably do not need to chop up the pdf-s (we moved past that), run `make pages` to only build the html pages.

## Modification

### Adding static pages

To add a static page/content, place it under `static/` directory. 
Then add a space-separated entry into `st_pages` variable inside the `Makefile`.
Then run `make`, and the page sould be copied to the output

### Adding new data

Edit the `data.xlsx` file with new content.
Add the new years in the `years` variable in the `Makefile`, and optionaly new `progs`.
Edit the `static/index.html` if needed to make links to new year/program pages (will be created).
Run `make` to generate new pages and update existing.

### Uploading the site

From `gen/` directory, do a `git commit` and `git push` to depoly new content.
