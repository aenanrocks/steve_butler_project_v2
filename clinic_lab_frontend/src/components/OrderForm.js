import React, { useState } from 'react';
import axios from 'axios';

const OrderForm = () => {
    const [deliveryMethod, setDeliveryMethod] = useState('email');
    const [notes, setNotes] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:8000/api/orders/', {
                delivery_method: deliveryMethod,
                notes,
            }, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access_token')}`,
                },
            });
            alert('Order created successfully');
        } catch (error) {
            console.error('Error creating order', error);
        }
    };

    return (
        <div>
            <h2>Create New Order</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Delivery Method</label>
                    <select
                        value={deliveryMethod}
                        onChange={(e) => setDeliveryMethod(e.target.value)}
                    >
                        <option value="email">Email</option>
                        <option value="post">Post</option>
                        <option value="pickup">Pickup</option>
                    </select>
                </div>
                <div>
                    <label>Notes</label>
                    <textarea
                        value={notes}
                        onChange={(e) => setNotes(e.target.value)}
                    />
                </div>
                <button type="submit">Submit Order</button>
            </form>
        </div>
    );
};

export default OrderForm;
