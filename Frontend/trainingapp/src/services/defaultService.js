import axios from 'axios';

export async function getEventsByDate( startDate, endDate) {
    var promise = await axios.get('http://127.0.0.1:8000/Trainings/' + startDate + '/' + endDate + '/')
    var dataFromServer = JSON.parse(promise.data)
    return dataFromServer
}