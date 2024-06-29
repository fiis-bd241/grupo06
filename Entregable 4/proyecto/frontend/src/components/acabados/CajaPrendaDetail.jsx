// src/components/CajaPrendaDetail.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const CajaPrendaDetail = () => {
  const { id_caja } = useParams();
  const [caja, setCaja] = useState(null);

  useEffect(() => {
    axios.get(`/api/cajas/${id_caja}/`)
      .then(response => setCaja(response.data))
      .catch(error => console.error(error));
  }, [id_caja]);

  if (!caja) return <div>Loading...</div>;

  return (
    <div>
      <h2>Detalles de Caja {caja.id_caja}</h2>
      <p>Tipo Prenda: {caja.tipo_prenda}</p>
      <p>Cantidad: {caja.cantidad}</p>
      <p>Fecha Creación: {caja.fecha_creacion}</p>
      <p>Estado: {caja.estado}</p>
      <p>ID Dim Confección: {caja.id_dim_confeccion}</p>
      <p>ID Guía Confección: {caja.id_guia_confeccion}</p>
    </div>
  );
};

export default CajaPrendaDetail;
