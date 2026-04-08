import axios from 'axios'

const baseUrl = "http://localhost:3001/persons"

const create = (personObject) => {
  return axios.post(baseUrl, personObject)
    .then(response => response.data)
}

const deletePerson = (personObject) => {
  return axios.delete(`${baseUrl}/${personObject.id}`)
}

export default {create, deletePerson}