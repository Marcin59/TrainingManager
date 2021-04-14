import axios from 'axios';

export async function getTrainingsByDate( startDate, endDate) {
    var promise = await axios.get('http://127.0.0.1:8000/Trainings/' + startDate + '/' + endDate + '/')
    var dataFromServer = JSON.parse(promise.data)
    return dataFromServer
}

export function postNewTraining(data) {
    axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/Trainings/',
        data: data
      });
}

export async function getExerciseTitles() {
    var promise = await axios.get('http://127.0.0.1:8000/Trainings/ExerciseTitles')
    var dataFromServer = JSON.parse(promise.data)
    return dataFromServer
}