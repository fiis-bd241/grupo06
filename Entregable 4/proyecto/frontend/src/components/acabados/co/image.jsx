import React, { useState } from 'react';
import { Tooltip, ClickAwayListener, Button } from '@mui/material';
import { styled } from '@mui/system';

const StyledTooltipContent = styled('div')({
  width: '900px',
 // height: '500px',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  backgroundColor: 'transparent',
  padding: '0',
  margin: '0',
});

const Image = styled('img')({
  width: '100%',
  height: '100%',
  objectFit: 'cover',
});

const ImageTooltip = ({ imageUrl }) => {
  const [open, setOpen] = useState(false);

  const handleTooltipClose = () => {
    setOpen(false);
  };

  const handleTooltipOpen = () => {
    setOpen(true);
  };

  return (
    <ClickAwayListener onClickAway={handleTooltipClose}>
      <div>
        <Tooltip
          PopperProps={{
            disablePortal: true,
          }}
          onClose={handleTooltipClose}
          open={open}
          disableFocusListener
          disableHoverListener
          disableTouchListener
          title={
            <StyledTooltipContent>
              <Image src={imageUrl} alt="Tooltip image" />
            </StyledTooltipContent>
          }
        >
          <Button onClick={handleTooltipOpen}>Ver SQL</Button>
        </Tooltip>
      </div>
    </ClickAwayListener>
  );
};

export default ImageTooltip;
