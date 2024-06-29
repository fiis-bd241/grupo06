import React, { useEffect, useState } from 'react';
import axios from 'axios';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';

const EmpleadoSelect = ({ idOperario, handleChange }) => {
  const [empleados, setEmpleados] = useState([]);

  useEffect(() => {
    axios.get('https://sistema-web-v.onrender.com/sistema/empleados')
      .then(response => setEmpleados(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <FormControl variant="outlined" fullWidth>
      <InputLabel id="id-operario-label">ID Operario</InputLabel>
      <Select
        labelId="id-operario-label"
        id="id-operario-select"
        value={idOperario}
        onChange={handleChange}
        label="ID Operario"
      >
        {empleados.map((empleado) => (
          <MenuItem key={empleado.nombre} value={empleado.nombre}>
            {empleado.nombre}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default EmpleadoSelect;
