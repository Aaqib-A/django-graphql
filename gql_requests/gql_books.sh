script='query {
    allBooks{
        id
        title
    }
}'
script="$(echo $script)"

curl -i -H 'Content-Type: application/json' \
   -X POST -d "{ \"query\": \"$script\"}" localhost:8000/books/graphql
