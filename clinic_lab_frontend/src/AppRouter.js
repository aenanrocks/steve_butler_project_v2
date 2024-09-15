import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

const Login = () => <div>Login Page</div>;
const Dashboard = () => <div>Dashboard Page</div>;

const AppRouter = () => (
  <Router>
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/" element={<Login />} />
    </Routes>
  </Router>
);

export default AppRouter;
