const express = require('express')
const morgan = require('morgan')

const app = express()
app.use(express.json())
app.use(morgan('tiny'))

let data = [
    { 
      "id": "1",
      "name": "Arto Hellas", 
      "number": "040-123456"
    },
    { 
      "id": "2",
      "name": "Ada Lovelace", 
      "number": "39-44-5323523"
    },
    { 
      "id": "3",
      "name": "Dan Abramov", 
      "number": "12-43-234345"
    },
    { 
      "id": "4",
      "name": "Mary Poppendieck", 
      "number": "39-23-6423122"
    }
]

app.get('/api/persons', (req, res) => {
  console.log("Hello from /")
  res.json(data)
})

app.get('/api/persons/:id', (req, res) => {
  res.json(data.find(el => el.id == req.params.id))
})

app.delete('/api/persons/:id', (req, res) => {
  data = data.filter(el => el.id !== req.params.id)
  res.json(data)
})

app.post('/api/persons', (req, res) => {
  const body = req.body

  // 1. Check if name or number is missing
  if (!body.name || !body.number) {
    return res.status(400).json({ 
      error: 'name or number missing' 
    })
  }

  // 2. Check if name already exists
  const nameExists = data.some(person => person.name === body.name)
  if (nameExists) {
    return res.status(400).json({ 
      error: 'name must be unique' 
    })
  }

  // 3. Generate ID and create new person object
  const maxId = 1000000
  const randomId = String(Math.floor(Math.random() * maxId))
  
  const newPerson = {
    id: randomId,
    name: body.name,
    number: body.number
  }

  data = data.concat(newPerson)
  res.json(newPerson)
})

app.get('/info', (req, res) => {
  const personCount = data.length
  const currentTime = new Date()
  
  res.send(`
    <p>Phonebook has info for ${personCount} people</p>
    <p>${currentTime}</p>
  `)
})


const PORT = 3001
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})