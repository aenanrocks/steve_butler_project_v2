import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Notifications from './components/Notifications';
import OrderForm from './components/OrderForm';

const AppRouter = () => (
    <Router>
        <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/notifications" element={<Notifications />} />
            <Route path="/orders/new" element={<OrderForm />} />
        </Routes>
    </Router>
);

export default AppRouter;
