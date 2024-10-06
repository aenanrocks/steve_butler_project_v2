import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Notifications = () => {
    const [notifications, setNotifications] = useState([]);

    useEffect(() => {
        // Fetch notifications from the backend
        const fetchNotifications = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/notifications/', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
                    },
                });
                setNotifications(response.data);
            } catch (error) {
                console.error('Error fetching notifications', error);
            }
        };
        fetchNotifications();

        // Connect to WebSocket for real-time notifications
        const socket = new WebSocket('ws://localhost:8000/ws/notifications/');

        // Listen for messages from WebSocket
        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setNotifications((prevNotifications) => [
                ...prevNotifications,
                { message: data.message, created_at: new Date().toLocaleString() },
            ]);
        };

        // Clean up WebSocket connection on component unmount
        return () => socket.close();
    }, []);

    return (
        <div>
            <h2>Notifications</h2>
            <ul>
                {notifications.map((notification, index) => (
                    <li key={index}>
                        {notification.message} - {notification.created_at}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Notifications;
