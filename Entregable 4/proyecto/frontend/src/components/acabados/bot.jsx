import React from 'react';
import { IconButton } from '@mui/material';
import HomeIcon from '@mui/icons-material/Home';
import { useNavigate } from 'react-router-dom';

const Bot = () => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/acabados/lotes');
  };

  return (
    <IconButton
      onClick={handleClick}
      sx={{
        backgroundColor: 'grey',
        color: 'white',
        '&:hover': {
          backgroundColor: 'darkgrey',
        },
        borderRadius: '8px', // Para mantener el botón cuadrado
      }}
    >
      <HomeIcon />
    </IconButton>
  );
};

export default Bot;
