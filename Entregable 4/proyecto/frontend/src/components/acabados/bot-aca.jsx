import React from 'react';
import { IconButton } from '@mui/material';
import HomeIcon from '@mui/icons-material/Home';
import { useNavigate } from 'react-router-dom';

const BotAca = () => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/acabados/acabados');
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

export default BotAca;
