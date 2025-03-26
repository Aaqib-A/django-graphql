script='query GetQuestion($id: Int=1)
{
    allQuizzes(id:$id) {
        id,
        title
    }
    allAnswers(id:$id){
        answerText
    }
}'
script="$(echo $script)"

curl -i -H 'Content-Type: application/json' \
   -X POST -d "{ \"query\": \"$script\"}" localhost:8000/quiz/graphql
