import "./App.css";
import Navbar from "./components/Navbar";
import UserForm from "./components/UserForm";
import UserList from "./components/UserList";
import { useState } from "react";

function App() {
  const [refresh, setRefresh] = useState(false);
  const [selectedUser, setSelectedUser] = useState(null);

  const reloadUsers = () => {
    setRefresh(!refresh);
  };

  return (
    <>
      <Navbar />

      <div className="container">
        <UserForm
          reloadUsers={reloadUsers}
          selectedUser={selectedUser}
          setSelectedUser={setSelectedUser}
        />

        <UserList
          refresh={refresh}
          setSelectedUser={setSelectedUser}
        />
      </div>
    </>
  );
}

export default App;