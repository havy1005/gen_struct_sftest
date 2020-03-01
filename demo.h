/*AAAAA_BBBBB_MODULE_BIT_DEFINE*/
typedef struct _AAAAA_16_BBBBB_LEVEL_Bits 
{
    uint16 NULL0:2;  
    uint16 NULL1:2;  
    uint16 NULL2:2;  
    uint16 NULL3:2;  
    uint16 NULL4:2;  
    uint16 NULL5:2; 
    uint16 NULL6:2; 
    uint16 NULL7:2;         
}AAAAA_16_BBBBB_LEVEL_Bits; 
typedef struct _AAAAA_8_BBBBB_Bits
{
    uint8 NULL0:1; 
    uint8 NULL1:1; 
    uint8 NULL2:1; 
    uint8 NULL3:1; 
    uint8 NULL4:1;  
    uint8 NULL5:1; 
    uint8 NULL6:1; 
    uint8 NULL7:1;               
}AAAAA_8_BBBBB_Bits;
typedef union
{
    uint16 U;                          
    sint16 I;                           
    AAAAA_16_BBBBB_LEVEL_Bits B;                    
}AAAAA_16_BBBBB_LEVEL;
typedef union
{
    uint8 U;                          
    sint8 I;                          
    AAAAA_8_BBBBB_Bits B;                    
}AAAAA_8_BBBBB;