
    import React, { useState, useEffect } from 'react';
    import { DataGrid } from '@mui/x-data-grid';
    import { Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from '@mui/material';
    import axios from 'axios';
    
    const App = () => {
        const [rows, setRows] = useState([]);
        const [open, setOpen] = useState(false);
        const [selectedRow, setSelectedRow] = useState(null);
        const [fechaActividad, setFechaActividad] = useState('');
        const [idMaquina, setIdMaquina] = useState('');
        const [cantidadHecha, setCantidadHecha] = useState('');
    
        useEffect(() => {
            axios.get('https://sistema-web-v.onrender.com/sistema/ordenes-produccion/')
                .then(response => {
                    const dataWithId = response.data.map(item => ({
                        ...item,
                        id: item.id_orden_producción
                    }));
                    setRows(dataWithId);
                });
        }, []);
    
        const handleAsignarClick = (row) => {
            setSelectedRow(row);
            setOpen(true);
        };
    
        const handleClose = () => {
            setOpen(false);
            setFechaActividad('');
            setIdMaquina('');
            setCantidadHecha('');
        };
    
        const handleSubmit = () => {
            axios.post('https://sistema-web-v.onrender.com/sistema/ordenes-produccion/asignar/', {
                fecha_actividad: fechaActividad,
                id_orden_produccion: selectedRow.id_orden_producción,
                id_maquina: idMaquina,
                cantidad_hecha: cantidadHecha
            }).then(response => {
                handleClose();
            });
        };
    
        const columns = [
            { field: 'id_orden_producción', headerName: 'ID Orden Producción', width: 200 },
            { field: 'fecha_inicio', headerName: 'Fecha Inicio', width: 150 },
            { field: 'fecha_fin', headerName: 'Fecha Fin', width: 150 },
            { field: 'cantidad', headerName: 'Cantidad', width: 100 },
            { field: 'estado_orden', headerName: 'Estado Orden', width: 150 },
            { field: 'area', headerName: 'Area', width: 100 },
            { field: 'tipo_corte', headerName: 'Tipo Corte', width: 150 },
            { field: 'tipo_materia_prima', headerName: 'Tipo Materia Prima', width: 150 },
            { field: 'id_orden_trabajo', headerName: 'ID Orden Trabajo', width: 200 },
            { field: 'fecha_creacion', headerName: 'Fecha Creación', width: 150 },
            {
                field: 'asignar',
                headerName: 'Asignar',
                width: 80,
                renderCell: (params) => (
                    <Button variant="contained" color="primary" onClick={() => handleAsignarClick(params.row)}>
                        Asignar
                    </Button>
                )
            }
        ];
    
        return (
            <div style={{ height: 400, width: '70%' }}>
                <DataGrid 
                    rows={rows} 
                    columns={columns} 
                    pageSize={10} 
                    getRowId={(row) => row.id_orden_producción}
                />
                <Dialog open={open} onClose={handleClose}>
                    <DialogTitle>Asignar</DialogTitle>
                    <DialogContent>
                        <TextField
                            autoFocus
                            margin="dense"
                            label="Fecha Actividad"
                            type="date"
                            fullWidth
                            value={fechaActividad}
                            onChange={(e) => setFechaActividad(e.target.value)}
                        />
                        <TextField
                            margin="dense"
                            label="ID Máquina"
                            type="number"
                            fullWidth
                            value={idMaquina}
                            onChange={(e) => setIdMaquina(e.target.value)}
                        />
                        <TextField
                            margin="dense"
                            label="Cantidad Hecha"
                            type="number"
                            fullWidth
                            value={cantidadHecha}
                            onChange={(e) => setCantidadHecha(e.target.value)}
                        />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose} color="primary">
                            Cancelar
                        </Button>
                        <Button onClick={handleSubmit} color="primary">
                            Asignar
                        </Button>
                    </DialogActions>
                </Dialog>
            </div>
        );
    };
    
    export default App;
    