import React, { useState } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button, TextField } from '@mui/material';

const InsertDataTableC = () => {
    const [data, setData] = useState([]);
    const [formData, setFormData] = useState({
        cantidad: '',
        id_dim_corte: '',
        id_estado: '',
        id_actividad: '',
        fecha_creacion: '',
        cantidad_usada: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('https://sistema-web-v.onrender.com/sistema/insertar/', formData);
            if (response.data.success) {
                setData([...data, { id_lote: response.data.id_lote, ...formData }]);
                setFormData({
                    cantidad: '',
                    id_dim_corte: '',
                    id_estado: '',
                    id_actividad: '',
                    fecha_creacion: '',
                    cantidad_usada: ''
                });
            }
        } catch (error) {
            console.error('There was an error inserting the data!', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <TextField name="cantidad" label="Cantidad" value={formData.cantidad} onChange={handleChange} />
                <TextField name="id_dim_corte" label="ID Dim Corte" value={formData.id_dim_corte} onChange={handleChange} />
                <TextField name="id_estado" label="ID Estado" value={formData.id_estado} onChange={handleChange} />
                <TextField name="id_actividad" label="ID Actividad" value={formData.id_actividad} onChange={handleChange} />
                <TextField name="fecha_creacion" label="Fecha Creación" value={formData.fecha_creacion} onChange={handleChange} />
                <TextField name="cantidad_usada" label="Cantidad Usada" value={formData.cantidad_usada} onChange={handleChange} />
                <Button type="submit" variant="contained" color="primary">Insertar</Button>
            </form>

            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>ID Lote</TableCell>
                            <TableCell>Cantidad</TableCell>
                            <TableCell>ID Dim Corte</TableCell>
                            <TableCell>ID Estado</TableCell>
                            <TableCell>ID Actividad</TableCell>
                            <TableCell>Fecha Creación</TableCell>
                            <TableCell>Cantidad Usada</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {data.map((row, index) => (
                            <TableRow key={index}>
                                <TableCell>{row.id_lote}</TableCell>
                                <TableCell>{row.cantidad}</TableCell>
                                <TableCell>{row.id_dim_corte}</TableCell>
                                <TableCell>{row.id_estado}</TableCell>
                                <TableCell>{row.id_actividad}</TableCell>
                                <TableCell>{row.fecha_creacion}</TableCell>
                                <TableCell>{row.cantidad_usada}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </div>
    );
};

export default InsertDataTableC;
