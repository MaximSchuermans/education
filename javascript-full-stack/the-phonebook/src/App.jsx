import { useState, useEffect } from "react";
import personService from "./services/persons";
import axios from "axios";

const Notification = ({ message, type }) => {
  if (message === null) {
    return null;
  }

  const notificationStyle = {
    color: type === "error" ? "red" : "green",
    background: "lightgrey",
    fontSize: 20,
    borderStyle: "solid",
    borderRadius: 5,
    padding: 10,
    marginBottom: 10,
  };

  return <div style={notificationStyle}>{message}</div>;
};

const Person = ({ person, deletePerson }) => {
  return (
    <li>
      {person.name} {person.number}
      <button onClick={() => deletePerson(person)}>delete</button>
    </li>
  );
};

const Persons = ({ persons, deletePerson }) => {
  return (
    <ul>
      {persons.map((person) => (
        <Person key={person.id} person={person} deletePerson={deletePerson} />
      ))}
    </ul>
  );
};

const PersonForm = ({
  onSubmit,
  newName,
  handleNameChange,
  newNumber,
  handleNumberChange,
}) => {
  return (
    <form onSubmit={onSubmit}>
      <div>
        name: <input value={newName} onChange={handleNameChange} />
      </div>
      <div>
        number: <input value={newNumber} onChange={handleNumberChange} />
      </div>
      <div>
        <button type="submit">add</button>
      </div>
    </form>
  );
};

const App = () => {
  const [persons, setPersons] = useState([]);
  const [newName, setNewName] = useState("");
  const [newNumber, setNewNumber] = useState("");
  const [notification, setNotification] = useState({
    message: null,
    type: "success",
  });

  useEffect(() => {
    axios.get("http://localhost:3001/persons").then((response) => {
      setPersons(response.data);
    });
  }, []);

  const showNotification = (message, type = "success") => {
    setNotification({ message, type });
    setTimeout(() => {
      setNotification({ message: null, type: "success" });
    }, 5000);
  };

  const addPerson = (event) => {
    event.preventDefault();

    const trimmedName = newName.trim();
    const trimmedNumber = newNumber.trim();

    if (!trimmedName || !trimmedNumber) {
      alert("Both name and number are required");
      return;
    }

    const isDuplicate = persons.some(
      (person) => person.name.toLowerCase() === trimmedName.toLowerCase(),
    );

    if (isDuplicate) {
      alert(`${trimmedName} is already added to phonebook`);
      return;
    }

    const personObject = {
      name: trimmedName,
      number: trimmedNumber,
    };

    personService
      .create(personObject)
      .then((data) => {
        setPersons(persons.concat(data));
        showNotification(`Added ${data.name}`);
        setNewName("");
        setNewNumber("");
      })
      .catch((error) => {
        showNotification(`Could not add ${trimmedName}`, "error");
      });
  };

  const deletePerson = (person) => {
    if (window.confirm(`Delete ${person.name}?`)) {
      personService
        .deletePerson(person)
        .then(() => {
          setPersons(persons.filter((p) => p.id !== person.id));
          showNotification(`Deleted ${person.name}`);
        })
        .catch((error) => {
          showNotification(
            `Information of ${person.name} has already been removed from server`,
            "error",
          );
          setPersons(persons.filter((p) => p.id !== person.id));
        });
    }
  };

  const handleNameChange = (event) => setNewName(event.target.value);
  const handleNumberChange = (event) => setNewNumber(event.target.value);

  return (
    <div>
      <h2>Phonebook</h2>
      <Notification message={notification.message} type={notification.type} />
      <PersonForm
        onSubmit={addPerson}
        newName={newName}
        handleNameChange={handleNameChange}
        newNumber={newNumber}
        handleNumberChange={handleNumberChange}
      />
      <h2>Numbers</h2>
      <Persons persons={persons} deletePerson={deletePerson} />
    </div>
  );
};

export default App;
