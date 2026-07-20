import { useState, useEffect } from "react";
import API from "../services/api";

function UserForm({
  reloadUsers,
  selectedUser,
  setSelectedUser,
}) {
  const [user, setUser] = useState({
    name: "",
    email: "",
    age: "",
  });

  useEffect(() => {
    if (selectedUser) {
      setUser(selectedUser);
    }
  }, [selectedUser]);

  const handleChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (selectedUser) {
        await API.put(`/users/${selectedUser.id}`, user);

        alert("User Updated Successfully!");

        setSelectedUser(null);
      } else {
        await API.post("/users", user);

        alert("User Added Successfully!");
      }

      setUser({
        name: "",
        email: "",
        age: "",
      });

      reloadUsers();
    } catch (error) {
      console.error(error);
      alert("Operation Failed");
    }
  };

  return (
    <div className="card">
      <h2>{selectedUser ? "Edit User" : "Add User"}</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Enter Name"
          value={user.name}
          onChange={handleChange}
          className="input"
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Enter Email"
          value={user.email}
          onChange={handleChange}
          className="input"
          required
        />

        <input
          type="number"
          name="age"
          placeholder="Enter Age"
          value={user.age}
          onChange={handleChange}
          className="input"
          required
        />

        <button className="btn">
          {selectedUser ? "Update User" : "Add User"}
        </button>
      </form>
    </div>
  );
}

export default UserForm;