script='query {
  repositoryOwner(login:\"danbst\") {
    repositories(first: 100) {
      edges {
        node {
          nameWithOwner
          pullRequests(last: 100, states: OPEN) {
            edges {
              node {
                title
                url
                author {
                  login
                }
                labels(first: 20) {
                  edges {
                    node {
                      name
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}'
script="$(echo $script)"   # the query should be a one-liner, without newlines

curl -i -H 'Content-Type: application/json' \
   -H "Authorization: bearer ........." \
   -X POST -d "{ \"query\": \"$script\"}" https://api.github.com/graphql
