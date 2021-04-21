import axios from 'axios';

export async function getStatistics() {
    var promise = await axios.get('http://127.0.0.1:8000/Statistics/')
    var dataFromServer = JSON.parse(promise.data)
    return dataFromServer
}

export async function getStatisticTitles() {
    var promise = await axios.get('http://127.0.0.1:8000/Statistics/Titles/')
    var dataFromServer = JSON.parse(promise.data)
    return dataFromServer
}

export async function postNewStatistic(data) {
    await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/Statistics/',
        data: data
      });
}