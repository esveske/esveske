#!/bin/bash

if [[ -n $1 ]]
then
    echo "<url><loc>https://esveske.github.io$1</loc><lastmod>$(date -I -r .$1)</lastmod></url>"
    exit 0
else
    FF=$(readlink --canonicalize $0)

    cd gen

    echo '<?xml version="1.0" encoding="UTF-8"?>'
    echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    find . -not -wholename '*/.*' | \
        sed 's/.//' | \
        xargs -n 1 $FF

    echo '</urlset>'
fi