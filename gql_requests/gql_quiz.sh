script='query{
  allQuizzes {
    id,
    title
  },
  allQuestions{
    title,
    quiz{
      id,
      title,
    },
    
  }
}'
script="$(echo $script)"

curl -i -H 'Content-Type: application/json' \
   -X POST -d "{ \"query\": \"$script\"}" localhost:8000/quiz/graphql
