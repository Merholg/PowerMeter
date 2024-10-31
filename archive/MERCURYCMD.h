//---------------------------------------------------------------------------

#ifndef MERCURYCMDH
#define MERCURYCMDH

#include "COMMPORT.h"

//---------------------------------------------------------------------------
#define ONEBYTE_0x00h L"�������."
#define ONEBYTE_0x01h L"������������ ������� ��� ��������."
#define ONEBYTE_0x02h L"���������� ������ ��������."
#define ONEBYTE_0x03h L"�� ���������� ������� ������� ��� �������������� �������."
#define ONEBYTE_0x04h L"���������� ���� �������� ��� ���������������� � ������� ������� �����."
#define ONEBYTE_0x05h L"�� ������ ����� �����."

#define Condition_Temperature L"����������� �������"
#define Condition_E01 L"���������� ��������� ���� 2,2(�)"
#define Condition_E02 L"�������� ���������������� ������2"
#define Condition_E03 L"�������� ���������������� UART"
#define Condition_E04 L"�������� ���������������� ADS"
#define Condition_E05 L"������ ������ � ������� 1"
#define Condition_E06 L"������������� �����"
#define Condition_E07 L"�������� ���������������� ������ 3"
#define Condition_E09 L"������ �� ��"
#define Condition_E10 L"������ ������������� �������������"
#define Condition_E11 L"������ ��������� ����������� �������"
#define Condition_E12 L"������ �������� ������"
#define Condition_E13 L"������ ��������� ������"
#define Condition_E14 L"��������� ������"
#define Condition_E15 L"������ ������� ��������� ����������"
#define Condition_E16 L"��������� ���� ������������"
#define Condition_E17 L"��������� ���� ���������� ��������"
#define Condition_E18 L"������ ������ ��������"
#define Condition_E19 L"������ ������ �������"
#define Condition_E20 L"��������� ���������� UART"
#define Condition_E21 L"������ ���������� ��������� �� �������"
#define Condition_E22 L"������ ���������� ��������� �� ��������"
#define Condition_E23 L"����������� ��������� ��������"
#define Condition_E24 L"��������� ���� ��������������� ������"
#define Condition_E25 L"���������� ���������� ����������� ����"
#define Condition_E26 L"���������� �������� ����������"
#define Condition_E27 L"��������� ������ �������"
#define Condition_E28 L"������ �������� ���������"
#define Condition_E29 L"������ �������������� �������"
#define Condition_E30 L"���������� ������������ �������������"
#define Condition_E31 L"���������� �������� ����������"
#define Condition_E32 L"������ ���������� �����"
#define Condition_E33 L"���������� �������� �����"
#define Condition_E34 L"������ ���������� ������� �������"
#define Condition_E35 L"������ ������ ������� �������"
#define Condition_E36 L"����������� �������� ����� ����������� ������"
#define Condition_E37 L"������ ��������� ����������� ������"
#define Condition_E38 L"������ ��������� ����������� ������� ������"
#define Condition_E39 L"���������� �������� ��������� �����"
#define Condition_E40 L"���� ����������� ���������. ���������"
#define Condition_E41 L"����������� ���������� ������� ���"
#define Condition_E42 L"������ ������ ������� ���"
#define Condition_E47 L"���������� ��������� ��������� �������"
#define Condition_E48 L"���������� ��������� ���� 2,65(�)"

#define Consist_SoftVer L"������ �� ��������"
#define Consist_In L"I� I� - ����������� ��� (�)"
#define Consist_Un L"U� U� - ����������� ���������� (�)"
#define Consist_ClR L"Cl R ����� �������� �� ���������� ������� (%)"
#define Consist_ClA L"Cl � ����� �������� �� �������� ������� (%)"
#define Consist_MeterConst L"���������� �������� (���./���*�)"
#define Consist_NPhase L"����� ���"
#define Consist_ProfMPower L"���� ������� ������� ���������"
#define Consist_TempRange L"������������� �������� (�C)"
#define Consist_NDirect L"����� �����������"
#define Consist_NVarProd_Un L"����������� ���������� (�)"
#define Consist_NVarProd_In L"����������� ��� (�)"
#define Consist_NVarProd_Imax L"������������ ��� (�)"
#define Consist_NVarProd_MConst L"���������� ��������, ���./���*�"
#define Consist_MeterType L"��� ��������"
#define Consist_Tarificator L"�����������"
#define Consist_SumPhase L"������������ ���"
#define Consist_EPlonb L"��. ����� ������� ������"
#define Consist_ExSupp L"������� �������"
#define Consist_IFace L"���������"
#define Consist_OPort L"��������"
#define Consist_ModemGSM L"����� GSM"
#define Consist_ModemPLM L"����� PLC"
#define Consist_Mem3 L"������ No3"
#define Consist_PhCalcPower L"�������� ���� ������� A+"
#define Consist_QPower L"�������� ���"
#define Consist_SupIF1 L"���������� ������� ���������� 1"
#define Consist_IFace2 L"��������� 2"
#define Consist_CEPlomb L"���� ������� ��. ������ �������� ������"
#define Consist_TarMax L"���� ����������� ����� ���������� ��������"
#define Consist_Light L"���� ������� ��������� ���"
#define Consist_Relay L"���� ������� ����������� ����"
#define Consist_ExControl L"���� ������� ���������� ������� ���������� �������� ������������ ���������� ��������"
#define Consist_VoltTarif L"���� ������������ ������� ������� �����������"
#define Consist_BEPlomb L"���� ������� ��.������ ���������� ������"
#define Consist_Profile2 L"���� ������� ������� 2"
#define Consist_ModemPLC2 L"����� PLC2"
#define Consist_IEC61107 L"���� ��������� IEC61107"
#define Consist_Kvolt L"����������� ������������� �� ����������"
#define Consist_Kcurr L"����������� ������������� �� ����"

#define ElectroVal_Voltage_Phase1 L"���������� ���� 1 (�)"
#define ElectroVal_Voltage_Phase2 L"���������� ���� 2 (�)"
#define ElectroVal_Voltage_Phase3 L"���������� ���� 3 (�)"
#define ElectroVal_Current_Phase1 L"��� ���� 1 (�)"
#define ElectroVal_Current_Phase2 L"��� ���� 2 (�)"
#define ElectroVal_Current_Phase3 L"��� ���� 3 (�)"
#define ElectroVal_Angle_Phase1 L"���� ����� ������������ ��� 1-2 (�)"
#define ElectroVal_Angle_Phase2 L"���� ����� ������������ ��� 1-3 (�)"
#define ElectroVal_Angle_Phase3 L"���� ����� ������������ ��� 2-3 (�)"
#define ElectroVal_PowerFactor_SumPhase L"����������� �������� ����� ���"
#define ElectroVal_PowerFactor_Phase1 L"����������� �������� cos� ���� 1"
#define ElectroVal_PowerFactor_Phase2 L"����������� �������� cos� ���� 2"
#define ElectroVal_PowerFactor_Phase3 L"����������� �������� cos� ���� 3"
#define ElectroVal_KADirect_SumPhase L"����������� �������� �������� ����� ���"
#define ElectroVal_KADirect_Phase1 L"����������� �������� �������� ���� 1"
#define ElectroVal_KADirect_Phase2 L"����������� �������� �������� ���� 2"
#define ElectroVal_KADirect_Phase3 L"����������� �������� �������� ���� 3"
#define ElectroVal_KRDirect_SumPhase L"����������� ���������� �������� ����� ���"
#define ElectroVal_KRDirect_Phase1 L"����������� ���������� �������� ���� 1"
#define ElectroVal_KRDirect_Phase2 L"����������� ���������� �������� ���� 2"
#define ElectroVal_KRDirect_Phase3 L"����������� ���������� �������� ���� 3"
#define ElectroVal_PPower_SumPhase L"�������� �������� P(����) ����� ���"
#define ElectroVal_PPower_Phase1 L"�������� �������� P(����) ���� 1"
#define ElectroVal_PPower_Phase2 L"�������� �������� P(����) ���� 2"
#define ElectroVal_PPower_Phase3 L"�������� �������� P(����) ���� 3"
#define ElectroVal_PADirect_SumPhase L"����������� �������� �������� ����� ���"
#define ElectroVal_PADirect_Phase1 L"����������� �������� �������� ���� 1"
#define ElectroVal_PADirect_Phase2 L"����������� �������� �������� ���� 2"
#define ElectroVal_PADirect_Phase3 L"����������� �������� �������� ���� 3"
#define ElectroVal_QPower_SumPhase L"���������� �������� Q(��� - ����� ����� ����������) ����� ���"
#define ElectroVal_QPower_Phase1 L"���������� �������� Q(��� - ����� ����� ����������) ���� 1"
#define ElectroVal_QPower_Phase2 L"���������� �������� Q(��� - ����� ����� ����������) ���� 2"
#define ElectroVal_QPower_Phase3 L"���������� �������� Q(��� - ����� ����� ����������) ���� 3"
#define ElectroVal_QRDirect_SumPhase L"����������� ���������� �������� ����� ���"
#define ElectroVal_QRDirect_Phase1 L"����������� ���������� �������� ���� 1"
#define ElectroVal_QRDirect_Phase2 L"����������� ���������� �������� ���� 2"
#define ElectroVal_QRDirect_Phase3 L"����������� ���������� �������� ���� 3"
#define ElectroVal_SPower_SumPhase L"������ �������� S(�� - ����� �����) ����� ���"
#define ElectroVal_SPower_Phase1 L"������ �������� S(�� - ����� �����) ���� 1"
#define ElectroVal_SPower_Phase2 L"������ �������� S(�� - ����� �����) ���� 2"
#define ElectroVal_SPower_Phase3 L"������ �������� S(�� - ����� �����) ���� 3"
#define ElectroVal_SADirect_SumPhase L"����������� �������� �������� ����� ���"
#define ElectroVal_SADirect_Phase1 L"����������� �������� �������� ���� 1"
#define ElectroVal_SADirect_Phase2 L"����������� �������� �������� ���� 2"
#define ElectroVal_SADirect_Phase3 L"����������� �������� �������� ���� 3"
#define ElectroVal_SRDirect_SumPhase L"����������� ���������� �������� ����� ���"
#define ElectroVal_SRDirect_Phase1 L"����������� ���������� �������� ���� 1"
#define ElectroVal_SRDirect_Phase2 L"����������� ���������� �������� ���� 2"
#define ElectroVal_SRDirect_Phase3 L"����������� ���������� �������� ���� 3"
#define ElectroVal_Frequency L"������� (��)"
#define ElectroVal_Distortion_Phase1 L"����������� ��������� ���������������� ������� ���������� ���� 1"
#define ElectroVal_Distortion_Phase2 L"����������� ��������� ���������������� ������� ���������� ���� 2"
#define ElectroVal_Distortion_Phase3 L"����������� ��������� ���������������� ������� ���������� ���� 3"


#pragma pack (push, 1)
struct DEFAULTPASSWORD
{
	unsigned char	DPass1;
	unsigned char	DPass2;
	unsigned char	DPass3;
	unsigned char	DPass4;
	unsigned char	DPass5;
	unsigned char	DPass6;
};
#pragma pack (pop)
#define DEFAULTPASSWORDLEN sizeof(DEFAULTPASSWORD)
#define EXPECT_DEFAULTPASSWORDLEN 6
#define MINLEVELACCESS 0x01
#define MAXLEVELACCESS 0x02

#pragma pack (push, 1)
struct LONGLONG8BYTE
{
	unsigned char	HiByte1;
	unsigned char	Byte2;
	unsigned char	Byte3;
	unsigned char	Byte4;
	unsigned char	Byte5;
	unsigned char	Byte6;
	unsigned char	Byte7;
	unsigned char	LoByte8;
};
#pragma pack (pop)

//2.3.1 ������ ��������� ������ �������� � ���� �������.
//� ����� �� ������ ������� ���������� 7 ���� � ���� ������ ������. ������ 4 ����� - ��-
//������ ����� � �������� ����������� ����, ��������� 3 ����� - ���� ������� � 2/10-� ����
//� ������������������: �����, �����, ���.
#pragma pack (push, 1)
struct METERDATA
{
	unsigned char		ZeroByte; //������������ � 8 ������ SN � ProdData
	unsigned char		SN1;      //  ��������
	unsigned char		SN2;      //          �����
	unsigned char		SN3;      //               �������
	unsigned char		SN4;      //                      �����
	unsigned char		ProdDay;     //  ����
	unsigned char		ProdMonth;   //      ������������
	unsigned char		ProdYear;    //                  �������
	unsigned char		Address; // �� 0 ����� ������ �� ����� ������ ����������� �� �������
	unsigned char		Result;  // ��� ������������ ��������� ��������
	unsigned char		Level; //  ������� ������� �������������� ���������� ���� ����������� �������
	unsigned char		DisableRead; // ����� ����������� - ������ ������� ���������
	unsigned char		ZeroPass1; // ������������ Pass � 8 ������
	unsigned char		ZeroPass2;
	unsigned char		Pass[DEFAULTPASSWORDLEN]; // ������ ������� � ����� �������
	unsigned long long	MercuryID; // ID �������� 00 SN1 SN2 SN3 SN4 ProdDay ProdMonth ProdYear
	unsigned long long	AccessPassword; // ������ 00 00 Pass[0] Pass[1] Pass[2] Pass[3] Pass[4] Pass[5]
};
#pragma pack (pop)
#define METERDATALEN sizeof(METERDATA)
#define MINMERCURYADDRESS 0x01
#define MAXMERCURYADDRESS 0xFD

#define REQSEQUENCLEN 8
#define RESPSTRUCRLEN 256
#pragma pack (push, 1)
struct EXCHANGEMETER
{
	BYTE   ReqSequenc[REQSEQUENCLEN];
	int    ReqSequencIdx;
	BYTE   RespStruct[RESPSTRUCRLEN];
	int    RespStructIdx;
};
#pragma pack (pop)

//����� �������
struct METERDATETIME
{
	TDateTime	Val;
	int			WeekDay;
	bool		Winter;
};

//��������� �������
//TEMPERATURE	 	int	 		2.3.15.5 ����� ������� �� ������ ������ �����������. TEMPERATURE
//STATEWORD	 	WORDSTATE	 	2.3.11 ������ ����� ���������. STATEWORD
struct CONDITION
{
	int		Temperature; //����������� �������
	bool	E01; //  ���������� ��������� ���� 2,2(�)
	bool	E02; //  �������� ���������������� ������2
	bool	E03; //  �������� ���������������� UART
	bool	E04; //  �������� ���������������� ADS
	bool	E05; //  ������ ������ � �������1
	bool	E06; //  ������������� �����
	bool	E07; //  �������� ���������������� ������3
	bool	E09; //  ������ �� ��
	bool	E10; //  ������ ������������� �������������
	bool	E11; //  ������ ��������� ����������� �������
	bool	E12; //  ������ �������� ������
	bool	E13; //  ������ ��������� ������
	bool	E14; //  ��������� ������
	bool	E15; //  ������ ������� ��������� ����������
	bool	E16; //  ��������� ���� ������������
	bool	E17; //  ��������� ���� ���������� ��������
	bool	E18; //  ������ ������ ��������
	bool	E19; //  ������ ������ �������
	bool	E20; //  ��������� ���������� UART
	bool	E21; //  ������ ���������� ��������� �� �������
	bool	E22; //  ������ ���������� ��������� �� ��������
	bool	E23; //  ����������� ��������� ��������
	bool	E24; //  ��������� ���� ��������������� ������
	bool	E25; //  ���������� ���������� ����������� ����
	bool	E26; //  ���������� �������� ����������
	bool	E27; //  ��������� ������ �������
	bool	E28; //  ������ �������� ���������
	bool	E29; //  ������ �������������� �������
	bool	E30; //  ���������� ������������ �������������
	bool	E31; //  ���������� �������� ����������
	bool	E32; //  ������ ���������� �����
	bool	E33; //  ���������� �������� �����
	bool	E34; //  ������ ���������� ������� �������
	bool	E35; //  ������ ������ ������� �������
	bool	E36; //  ����������� �������� ����� ����������� ������
	bool	E37; //  ������ ��������� ����������� ������
	bool	E38; //  ������ ��������� ����������� ������� ������
	bool	E39; //  ���������� �������� ��������� �����
	bool	E40; //  ���� ����������� ���������. ���������
	bool	E41; //  ����������� ���������� ������� ���
	bool	E42; //  ������ ������ ������� ���
	bool	E47; //  ���������� ��������� ��������� �������
	bool	E48; //  ���������� ��������� ���� 2,65(�)
};

// ������ �������
//SOFTVERSION	 	VERSIONSOFT	 	2.3.4 ������ ������ �� ��������. SOFTVERSION
//PRODUCTIONVAR	 	VARPRODUCTION	2.3.16 ������ �������� ����������. PRODUCTIONVAR
//KOEFTRANSFORM	 	TRANSFORMKOEF	2.3.3 ������ ������������ ������������� ��������. KOEFTRANSFORM
struct PRODUCTVARNO
{
	double	Un;		// ����������� ����������, �
	double	In;		// ����������� ���, �
	double	Imax;	// ������������ ���, �
	int		MConst;	// ���������� ��������, ���./���*�
};
#define CONSISTSOFTVERLEN 16
#define CONSISTMETERTYPE 4
#define CONSISTTARIFICATOR 4
#define CONSISTSYMPHASE 4
#define CONSISTIFACE 8
#define CONSISTMEM3 8
struct CONSIST
{
	char			SoftVer[CONSISTSOFTVERLEN]; 	// ������ �� ��������
	double			In;          	// I� I� - ����������� ��� �: 0 - 5; 1 - 1; 2 - 10.
	double			Un;          	// U� U� - ����������� ���������� �: 0 - 57,7; 1 - 230.
	double			ClR;         	// Cl R ����� �������� �� ���������� ������� %: 0 - 0,2; 1 - 0,5; 2 - 1,0; 3 - 2,0.
	double			ClA;	     	// Cl � ����� �������� �� �������� ������� %: 0 - 0,2; 1 - 0,5; 2 - 1,0; 3 - 2,0.
//---------------------------------
	int				MeterConst;  	// ���������� �������� ���/���?� 0 - 5000; 1 - 25000; 2 - 1250; 3 - 500; 4 - 1000; 5 - 250.
	int				NPhase;      	// ����� ��� 0 - 3, 1 - 1
	bool			ProfMPower;  	// ���� ������� ������� ��������� 0 - ���, 1 - ��
	int				TempRange;   	// ������������� ��������C 0 � 20, 1 � 40
	int				NDirect;     	// ����� ����������� 0 - 2, 1 - 1
//---------------------------------
	PRODUCTVARNO	NVarProd;    	// No �������� ���������� 1 - 57,7�_(1)5�_10�_5000���./���*� 2 - 230�5�60�500���./���*� 3 - 230�5�100�250���./���*� 4 - 230�(1)5�10�1000���./���*�
	char			MeterType[CONSISTMETERTYPE];	// ��� �������� 0 - AR, 1 - A
	char			Tarificator[CONSISTTARIFICATOR];	// ����������� 0 - �������, 1 - ����������
	char			SumPhase[CONSISTSYMPHASE];    // ������������ ��� 0 - � ������ �����, 1 - �� ������
//---------------------------------
	bool			EPlonb;         // ��. ����� ������� ������ 0 - ���, 1 - ����
	bool			ExSupp;         // ������� ������� 0 - ���, 1 - ����
	char			IFace[CONSISTIFACE];       // ��������� 0 - CAN, 1 - RS-485, 2 - ������, 3 - ���
	bool			OPort;          // �������� 0 - ���, 1 - ����
	bool			ModemGSM;       // ����� GSM 0 - ���, 1 - ����
	bool			ModemPLM;       // ����� PLM 0 - ���, 1 - ����
	char			Mem3[CONSISTMEM3];        // ������ No3 0 - 65.5x8, 1 - 131x8
//---------------------------------
	bool			PhCalcPower;    // �������� ���� ������� A+ 0 - ���, 1 - ��
	bool			QPower;         // �������� ��� 0 - ���, 1 - ��
	bool			SupIF1;         // ���������� ������� ���������� 1 0 - ���, 1 - ��
	bool			IFace2;         // ��������� 2 0 - ���, 1 - ��
	bool			CEPlomb;        // ���� ������� ��. ������ �������� ������, 0 - ���, 1 - ����
	bool			TarMax;         // ���� ����������� ����� ���������� ��������, 0 - ���, 1 - ����
	bool			Light;          // ���� ������� ��������� ���, 0 - ���, 1 - ����
	bool			Relay;          // ���� ������� ����������� ����, 0 - ���, 1 - ����
//---------------------------------
	bool			ExControl;      // ���� ������� ���������� ������� ���������� �������� ������������ ���������� ��������, 0 - ���, 1 - ����
	bool			VoltTarif;      // ���� ������������ ������� ������� �����������, 0 - ���, 1 - ��
	bool			BEPlomb;        // ���� ������� ��.������ ���������� ������, 0 - ���, 1 - ����
	bool			Profile2;       // ���� ������� ������� 2 0 - ���, 1 - ����
	bool			ModemPLC2;      // ����� PLC2, 0 - ���, 1 - ����
	bool			IEC61107;       // ���� ��������� IEC61107, 0 - ���, 1 - ��
	double			Kvolt; 			// ����������� ������������� �� ����������
	double			Kcurr; 			// ����������� ������������� �� ����
};

//�������������� ���������
//VOLTAGE3PHASE	 	PHASE3VOLTAGE	 	//2.3.15.2 ����� ������� �� ������ ������ ����������. VOLTAGE3PHASE
//CURRENT3PHASE	 	PHASE3CURRENT	 	//2.3.15.2 ����� ������� �� ������ ������ ����. CURRENT3PHASE
//ANGLE3PHASE	 	PHASE3ANGLE		//2.3.15.2 ����� ������� �� ������ ������ ����� ����� ������� ������������. ANGLE3PHASE
//KOEFPOWER3PHASE	 	PHASE3KOEFPOWER	 	//2.3.15.3 ����� ������� �� ������ ������ ������������� �������� KOEFPOWER3PHASE
//POWER3PHASE	 	PHASE3POWER	 	//2.3.15.1 ����� ������� �� ������ ������ �������� �������� P(����). POWER3PHASE
//POWER3PHASE	 	PHASE3POWER	 	//2.3.15.1 ����� ������� �� ������ ������ ���������� �������� Q(��� - ����� ����� ����������). POWER3PHASE
//POWER3PHASE	 	PHASE3POWER	 	//2.3.15.1 ����� ������� �� ������ ������ ������ �������� S(�� - ����� �����). POWER3PHASE
//FREQUENCY	 	double	 		//2.3.15.4 ����� ������� �� ������ ������ ������� FREQUENCY
//KOEFPHASEDISTORT3PHASE 	PHASE3KOEFPHASEDISTORT	//2.3.15.5 ����� ������� �� ������ ������ ������������� ��������� ���������������� ������ ����������. KOEFPHASEDISTORT3PHASE
struct PHASE3
{
	double	Phase1;
	double	Phase2;
	double	Phase3;
};
struct PHASE3SUM
{
	double	SumPhase;
	double	Phase1;
	double	Phase2;
	double	Phase3;
};
struct DIRECTPHASE3SUM
{
	int	SumPhase;
	int	Phase1;
	int	Phase2;
	int	Phase3;
};
struct ELECTROVAL
{
	PHASE3			Voltage;
	PHASE3			Current;
	PHASE3			Angle;
	PHASE3SUM		PowerFactor;
	DIRECTPHASE3SUM	KADirect;
	DIRECTPHASE3SUM	KRDirect;
	PHASE3SUM		PPower;
	DIRECTPHASE3SUM	PADirect;
	PHASE3SUM		QPower;
	DIRECTPHASE3SUM	QRDirect;
	PHASE3SUM		SPower;
	DIRECTPHASE3SUM	SADirect;
	DIRECTPHASE3SUM	SRDirect;
	double		Frequency;
	PHASE3		Distortion;
};

//TIMEOFMETER	 	TDateTime	 	//2.1.1 ������ �������� �������. TIMEOFMETER

//2.1.1 ������ �������� �������. TIMEOFMETER
//���� ������ ������ �������� 8 ���� 2/10-�� ���� � ������������������: �������,
//������, ����, ���� ������, �����, �����, ���, ������� ����/���� (����=1, ����=0).
//�����: 80 43 14 16 03 27 02 08 01 (CRC) 16:14:43 ����� 27 ������� 2008 ����, ����.
#pragma pack (push, 1)
struct TIMEOFMETER
{
	BYTE	Sec;
	BYTE	Min;
	BYTE	Hour;
	BYTE	Week;
	BYTE	Day;
	BYTE	Month;
	BYTE	Year;
	BYTE	Winter;
};
#pragma pack (pop)
#define TIMEOFMETERLEN sizeof(TIMEOFMETER)
#define EXPECT_TIMEOFMETERLEN 8

//2.3.4 ������ ������ �� ��������. SOFTVERSION
//� ����� �� ������ ������� ���������� 3 ����� 2/10-�� ���� � ���� ������ ������.
//�����: 80 09 00 00 (CRC) ������ ��: 9.0.0
#pragma pack (push, 1)
struct SOFTVERSION
{
	BYTE SV1;
	BYTE SV2;
	BYTE SV3;
};
#pragma pack (pop)
#define SOFTVERSIONLEN sizeof(SOFTVERSION)
#define EXPECT_SOFTVERSIONLEN 3

//2.3.11 ������ ����� ���������. STATEWORD
//���� ������ ������ ������� �� 6 ����.
#pragma pack (push, 1)
struct STATEWORD
{
	BYTE	E33:1; //  ���������� �������� �����
	BYTE	E34:1; //  ������ ���������� ������� �������
	BYTE	E35:1; //  ������ ������ ������� �������
	BYTE	E36:1; //  ����������� �������� ����� ����������� ������
	BYTE	E37:1; //  ������ ��������� ����������� ������
	BYTE	E38:1; //  ������ ��������� ����������� ������� ������
	BYTE	E39:1; //  ���������� �������� ��������� �����
	BYTE	E40:1; //  ���� ����������� ���������. ���������
//-------------------
	BYTE	E41:1; //  ����������� ���������� ������� ���
	BYTE	E42:1; //  ������ ������ ������� ���
	BYTE	E43:1; //
	BYTE	E44:1; //
	BYTE	E45:1; //
	BYTE	E46:1; //
	BYTE	E47:1; //  ���������� ��������� ��������� �������
	BYTE	E48:1; //  ���������� ��������� ���� 2,65(�)
//-------------------
	BYTE	E17:1; //  ��������� ���� ���������� ��������
	BYTE	E18:1; //  ������ ������ ��������
	BYTE	E19:1; //  ������ ������ �������
	BYTE	E20:1; //  ��������� ���������� UART
	BYTE	E21:1; //  ������ ���������� ��������� �� �������
	BYTE	E22:1; //  ������ ���������� ��������� �� ��������
	BYTE	E23:1; //  ����������� ��������� ��������
	BYTE	E24:1; //  ��������� ���� ��������������� ������
//-------------------
	BYTE	E25:1; //  ���������� ���������� ����������� ����
	BYTE	E26:1; //  ���������� �������� ����������
	BYTE	E27:1; //  ��������� ������ �������
	BYTE	E28:1; //  ������ �������� ���������
	BYTE	E29:1; //  ������ �������������� �������
	BYTE	E30:1; //  ���������� ������������ �������������
	BYTE	E31:1; //  ���������� �������� ����������
	BYTE	E32:1; //  ������ ���������� �����
//-------------------
	BYTE	E01:1; //  ���������� ��������� ���� 2,2(�)
	BYTE	E02:1; //  �������� ���������������� ������2
	BYTE	E03:1; //  �������� ���������������� UART
	BYTE	E04:1; //  �������� ���������������� ADS
	BYTE	E05:1; //  ������ ������ � �������1
	BYTE	E06:1; //  ������������� �����
	BYTE	E07:1; //  �������� ���������������� ������3
	BYTE	E08:1; //
//-------------------
	BYTE	E09:1; //  ������ �� ��
	BYTE	E10:1; //  ������ ������������� �������������
	BYTE	E11:1; //  ������ ��������� ����������� �������
	BYTE	E12:1; //  ������ �������� ������
	BYTE	E13:1; //  ������ ��������� ������
	BYTE	E14:1; //  ��������� ������
	BYTE	E15:1; //  ������ ������� ��������� ����������
	BYTE	E16:1; //  ��������� ���� ������������
};
#pragma pack (pop)
#define STATEWORDLEN sizeof(STATEWORD)
#define EXPECT_STATEWORDLEN 6

//2.3.16 ������ �������� ����������. PRODUCTIONVAR
//���� ������ ������ ������� �� 6 ����
#pragma pack (push, 1)
struct PRODUCTIONVAR
{
	BYTE In:2;             // I� I� - ����������� ��� �: 0 - 5; 1 - 1; 2 - 10.
	BYTE Un:2;             // U� U� - ����������� ���������� �: 0 - 57,7; 1 - 230.
	BYTE ClR:2;            // Cl R ����� �������� �� ���������� ������� %: 0 - 0,2; 1 - 0,5; 2 - 1,0; 3 - 2,0.
	BYTE ClA:2;            // Cl � ����� �������� �� �������� ������� %: 0 - 0,2; 1 - 0,5; 2 - 1,0; 3 - 2,0.
//---------------------------------
	BYTE MeterConst:4;     // ���������� �������� ���/���?� 0 - 5000; 1 - 25000; 2 - 1250; 3 - 500; 4 - 1000; 5 - 250.
	BYTE NPhase:1;         // ����� ��� 0 - 3, 1 - 1
	BYTE ProfMPower:1;     // ���� ������� ������� ��������� 0 - ���, 1 - ��
	BYTE TempRange:1;      // ������������� ��������C 0 � 20, 1 � 40
	BYTE NDirect:1;        // ����� ����������� 0 - 2, 1 - 1
//---------------------------------
	BYTE NVarProd:4;       // No �������� ���������� 1 - 57,7�(1)5�10�5000���./���*� 2 - 230�5�60�500���./���*� 3 - 230�5�100�250���./���*� 4 - 230�(1)5�10�1000���./���*�
	BYTE MeterType:2;      // ��� �������� 0 - AR, 1 - A
	BYTE Tarificator:1;    // ����������� 0 - �������, 1 - ����������
	BYTE SumPhase:1;       // ������������ ��� 0 - � ������ �����, 1 - �� ������
//---------------------------------
	BYTE EPlonb:1;         // ��. ����� ������� ������ 0 - ���, 1 - ����
	BYTE ExSupp:1;         // ������� ������� 0 - ���, 1 - ����
	BYTE IFace:2;          // ��������� 0 - CAN, 1 - RS-485, 2 - ������, 3 - ���
	BYTE OPort:1;          // �������� 0 - ���, 1 - ����
	BYTE ModemGSM:1;       // ����� GSM 0 - ���, 1 - ����
	BYTE ModemPLM:1;       // ����� PLM 0 - ���, 1 - ����
	BYTE Mem3:1;           // ������ No3 0 - 65.5x8, 1 - 131x8
//---------------------------------
	BYTE PhCalcPower:1;    // �������� ���� ������� A+ 0 - ���, 1 - ��
	BYTE QPower:1;         // �������� ��� 0 - ���, 1 - ��
	BYTE SupIF1:1;         // ���������� ������� ���������� 1 0 - ���, 1 - ��
	BYTE IFace2:1;         // ��������� 2 0 - ���, 1 - ��
	BYTE CEPlomb:1;        // ���� ������� ��. ������ �������� ������, 0 - ���, 1 - ����
	BYTE TarMax:1;         // ���� ����������� ����� ���������� ��������, 0 - ���, 1 - ����
	BYTE Light:1;          // ���� ������� ��������� ���, 0 - ���, 1 - ����
	BYTE Relay:1;          // ���� ������� ����������� ����, 0 - ���, 1 - ����
//---------------------------------
	BYTE ExControl:1;      // ���� ������� ���������� ������� ���������� �������� ������������ ���������� ��������, 0 - ���, 1 - ����
	BYTE VoltTarif:1;      // ���� ������������ ������� ������� �����������, 0 - ���, 1 - ��
	BYTE BEPlomb:1;        // ���� ������� ��.������ ���������� ������, 0 - ���, 1 - ����
	BYTE Profile2:1;       // ���� ������� ������� 2 0 - ���, 1 - ����
	BYTE ModemPLC2:1;      // ����� PLC2, 0 - ���, 1 - ����
	BYTE IEC61107:1;       // ���� ��������� IEC61107, 0 - ���, 1 - ��
	BYTE Reserved1:1;      // Reserved
	BYTE Reserved2:1;      // Reserved
};
#pragma pack (pop)
#define PRODUCTIONVARLEN sizeof(PRODUCTIONVAR)
#define EXPECT_PRODUCTIONVARLEN 6

//2.3.3 ������ ������������ ������������� ��������. KOEFTRANSFORM
//� ����� �� ������ ������� ���������� 4 ����� � ���� ������ ������ � ������������������:
//��� �������� ����� ��, ��� �������� ����� ��
//�����: 80 00 01 00 01 (CRC)
//����������� ������������� �� ���������� �� = 1
//����������� ������������� �� ���� �� = 1
#pragma pack (push, 1)
struct KOEFTRANSFORM
{
	BYTE HiKvolt; //����������� ������������� �� ���������� ������� ����
	BYTE LoKvolt; //����������� ������������� �� ���������� ������� ����
	BYTE HiKcurr; //����������� ������������� �� ���� ������� ����
	BYTE LoKcurr; //����������� ������������� �� ���� ������� ����
};
#pragma pack (pop)
#define KOEFTRANSFORMLEN sizeof(KOEFTRANSFORM)
#define EXPECT_KOEFTRANSFORMLEN 4

//2.3.15 ������ ��������������� ����������. VOLTAGE3PHASE
#pragma pack (push, 1)
struct VOLTAGE
{
	BYTE V1; //���� 1
	BYTE V3; //���� 3
	BYTE V2; //���� 2
};
#pragma pack (pop)
#define VOLTAGELEN sizeof(VOLTAGE)
#define EXPECT_VOLTAGELEN 3
#define VOLTAGEMULTIPLIER 100.0

//2.3.15 ������ ��������������� ����������. CURRENT3PHASE
#pragma pack (push, 1)
struct CURRENT
{
	BYTE C1; //���� 1
	BYTE C3; //���� 3
	BYTE C2; //���� 2
};
#pragma pack (pop)
#define CURRENTLEN sizeof(CURRENT)
#define EXPECT_CURRENTLEN 3
#define CURRENTMULTIPLIER 1000.0

//2.3.15 ������ ��������������� ����������. ANGLE3PHASE
#pragma pack (push, 1)
struct ANGLE
{
	BYTE A1; //���� 1
	BYTE A3; //���� 3
	BYTE A2; //���� 2
};
#pragma pack (pop)
#define ANGLELEN sizeof(ANGLE)
#define EXPECT_ANGLELEN 3
#define ANGLEMULTIPLIER 100.0

//2.3.15 ������ ��������������� ����������. KOEFPOWER3PHASE
#pragma pack (push, 1)
struct KOEFPOWER
{
	BYTE K1          :6; //���� 1
	BYTE DirectRPower:1; // ����������� ���������� ��������: 0 � ������; 1 � ��������.
	BYTE DirectAPower:1; // ����������� �������� ��������: 0 � ������; 1 � ��������.
	BYTE K3          :8; //���� 3
	BYTE K2          :8; //���� 2
};
#pragma pack (pop)
#define KOEFPOWERLEN sizeof(KOEFPOWER)
#define EXPECT_KOEFPOWERLEN 3
#define KOEFPOWERMULTIPLIER 1000.0

//2.3.15 ������ ��������������� ����������. POWER3PHASE
#pragma pack (push, 1)
struct POWER
{
	BYTE P1          :6; //���� 1
	BYTE DirectRPower:1; // ����������� ���������� ��������: 0 � ������; 1 � ��������.
	BYTE DirectAPower:1; // ����������� �������� ��������: 0 � ������; 1 � ��������.
	BYTE P3          :8; //���� 4
	BYTE P2          :8; //���� 3
};
#pragma pack (pop)
#define POWERLEN sizeof(POWER)
#define EXPECT_POWERLEN 3
#define POWERMULTIPLIER 100.0

//2.3.15 ������ ��������������� ����������. FREQUENCY
#pragma pack (push, 1)
struct FREQUENCY
{
	BYTE F1; //���� 1
	BYTE F3; //���� 3
	BYTE F2; //���� 2
};
#pragma pack (pop)
#define FREQUENCYLEN sizeof(FREQUENCY)
#define EXPECT_FREQUENCYLEN 3
#define FREQUENCYMULTIPLIER 100.0

//2.3.15 ������ ��������������� ����������. KOEFPHASEDISTORT3PHASE
#pragma pack (push, 1)
struct KOEFPHASEDISTORT
{
	BYTE LoKpd; //����������� ��������� ���������������� ������ ���������� ������� ����
	BYTE HiKpd; //����������� ��������� ���������������� ������ ���������� ������� ����
};
#pragma pack (pop)
#define KOEFPHASEDISTORTLEN sizeof(KOEFPHASEDISTORT)
#define EXPECT_KOEFPHASEDISTORTLEN 2
#define KOEFPHASEDISTORTMULTIPLIER 100.0

//2.3.15 ������ ��������������� ����������. TEMPERATURE
#pragma pack (push, 1)
struct TEMPERATURE
{
	BYTE HiT; //����������� ������ ������� ������� ������� ����
	BYTE LoT; //����������� ������ ������� ������� ������� ����
};
#pragma pack (pop)
#define TEMPERATURELEN sizeof(TEMPERATURE)
#define EXPECT_TEMPERATURELEN 2


class MercuryCmd
{
	private:
		CommPort * Port;
		METERDATA MeterData[256];  // MeterData[0] ��� ����������� �����
		int       MeterDataLen;
		int		  AllMeterDataLen;
		BYTE      DefaultPassword[DEFAULTPASSWORDLEN];
		int       DefaultPasswordLen;
		BYTE	  AccessLevel;

	protected:
		BYTE read_DefaultPassword(int index)
		{
			if (index >= 0 && index < DefaultPasswordLen) return (DefaultPassword[index]);
			return(0);
		}
		void write_DefaultPassword(int index, BYTE newDefaultPassword)
		{
			if (index >= 0 && index < DefaultPasswordLen) DefaultPassword[index] = newDefaultPassword;
			return;
		}
		METERDATA read_MeterData(int index)
		{
			return (MeterData[index]);
		}
		int  read_AccessLevel()
		{
			return(AccessLevel);
		}
		void write_AccessLevel(int newAccessLevel)
		{
			if (newAccessLevel < MINLEVELACCESS || newAccessLevel > MAXLEVELACCESS) newAccessLevel = MINLEVELACCESS;
			AccessLevel = newAccessLevel;
			return;
		}
	public:
		__fastcall MercuryCmd(CommPort * WorkPort);
		__fastcall ~MercuryCmd();
		void __fastcall SetMeterRassword(BYTE Address, BYTE AccessLevel, DEFAULTPASSWORD Password);
		WORD __fastcall AssembleWord(BYTE HiByte1, BYTE LoByte2);
		DWORD __fastcall AssembleDWord(BYTE HiByte1, BYTE Byte2, BYTE Byte3, BYTE LoByte4);
		unsigned long long __fastcall AssembleULongLong(LONGLONG8BYTE * ll8b);
		void __fastcall DAssembleULongLong(unsigned long long ull, LONGLONG8BYTE * ll8b);
		void __fastcall CalculateCRC(BYTE * arrCRC, BYTE C);
		bool __fastcall SendCommand(BYTE Address, unsigned long ExpectedLen);
		bool __fastcall TestConnection(BYTE Address);
		bool __fastcall GetMeterInfo(BYTE Address);
		void __fastcall ClearMeterData(int MeterDataIdx);
		void __fastcall ClearAllMeterData();
		void __fastcall SearchMeter();
		bool __fastcall SetSecurity(BYTE Address, int AccessLevel, unsigned long long AccessPassword);
		bool __fastcall OpenChannel(BYTE Address);
		bool __fastcall CloseChannel(BYTE Address);
		bool __fastcall GetMeter(BYTE Address, EXCHANGEMETER * ExStruct); //������������� ��� ������ ��������� � �������� �������
		bool __fastcall GetMeterTime(BYTE Address, TIMEOFMETER * TimeOfMeter, METERDATETIME * MeterTime); //2.1.1 ������ �������� �������. TIMEOFMETER
		bool __fastcall GetMeterStateWord(BYTE Address, STATEWORD * StateWord, CONDITION * Condition); //2.3.11 ������ ����� ���������. STATEWORD
		bool __fastcall GetMeterSoftVersion(BYTE Address, SOFTVERSION * SoftVersion, CONSIST * Consist); //2.3.4 ������ ������ �� ��������. SOFTVERSION
		bool __fastcall GetMeterProdVar(BYTE Address, PRODUCTIONVAR * ProductionVar, CONSIST * Consist); //2.3.16 ������ �������� ����������. PRODUCTIONVAR
		bool __fastcall GetMeterTransform(BYTE Address, KOEFTRANSFORM * KoefTransform, CONSIST * Consist); //2.3.3 ������ ������������ ������������� ��������. KOEFTRANSFORM
		bool __fastcall GetMeterTemperature(BYTE Address, TEMPERATURE * Temperature, CONDITION * Condition); //2.3.15.5 ����� ������� �� ������ ������ �����������. TEMPERATURE
		bool __fastcall GetVoltage1(BYTE Address, VOLTAGE * Voltage, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����������. VOLTAGE3PHASE
		bool __fastcall GetVoltage2(BYTE Address, VOLTAGE * Voltage, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����������. VOLTAGE3PHASE
		bool __fastcall GetVoltage3(BYTE Address, VOLTAGE * Voltage, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����������. VOLTAGE3PHASE
		bool __fastcall GetCurrent1(BYTE Address, CURRENT * Current, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����. CURRENT3PHASE
		bool __fastcall GetCurrent2(BYTE Address, CURRENT * Current, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����. CURRENT3PHASE
		bool __fastcall GetCurrent3(BYTE Address, CURRENT * Current, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����. CURRENT3PHASE
		bool __fastcall GetAngle1(BYTE Address, ANGLE * Angle, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����� ����� ������� ������������. ANGLE3PHASE
		bool __fastcall GetAngle2(BYTE Address, ANGLE * Angle, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����� ����� ������� ������������. ANGLE3PHASE
		bool __fastcall GetAngle3(BYTE Address, ANGLE * Angle, ELECTROVAL * ElectroVal); //2.3.15.2 ����� ������� �� ������ ������ ����� ����� ������� ������������. ANGLE3PHASE
		bool __fastcall GetPowerFactorS(BYTE Address, KOEFPOWER * PowerFactor, ELECTROVAL * ElectroVal); //2.3.15.3 ����� ������� �� ������ ������ ������������� �������� KOEFPOWER3PHASE
		bool __fastcall GetPowerFactor1(BYTE Address, KOEFPOWER * PowerFactor, ELECTROVAL * ElectroVal); //2.3.15.3 ����� ������� �� ������ ������ ������������� �������� KOEFPOWER3PHASE
		bool __fastcall GetPowerFactor2(BYTE Address, KOEFPOWER * PowerFactor, ELECTROVAL * ElectroVal); //2.3.15.3 ����� ������� �� ������ ������ ������������� �������� KOEFPOWER3PHASE
		bool __fastcall GetPowerFactor3(BYTE Address, KOEFPOWER * PowerFactor, ELECTROVAL * ElectroVal); //2.3.15.3 ����� ������� �� ������ ������ ������������� �������� KOEFPOWER3PHASE
		bool __fastcall GetPowerPS(BYTE Address, POWER * PowerP, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ �������� �������� P(����). POWER3PHASE
		bool __fastcall GetPowerP1(BYTE Address, POWER * PowerP, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ �������� �������� P(����). POWER3PHASE
		bool __fastcall GetPowerP2(BYTE Address, POWER * PowerP, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ �������� �������� P(����). POWER3PHASE
		bool __fastcall GetPowerP3(BYTE Address, POWER * PowerP, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ �������� �������� P(����). POWER3PHASE
		bool __fastcall GetPowerQS(BYTE Address, POWER * PowerQ, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ���������� �������� Q(��� - ����� ����� ����������). POWER3PHASE
		bool __fastcall GetPowerQ1(BYTE Address, POWER * PowerQ, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ���������� �������� Q(��� - ����� ����� ����������). POWER3PHASE
		bool __fastcall GetPowerQ2(BYTE Address, POWER * PowerQ, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ���������� �������� Q(��� - ����� ����� ����������). POWER3PHASE
		bool __fastcall GetPowerQ3(BYTE Address, POWER * PowerQ, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ���������� �������� Q(��� - ����� ����� ����������). POWER3PHASE
		bool __fastcall GetPowerSS(BYTE Address, POWER * PowerS, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ������ �������� S(�� - ����� �����). POWER3PHASE
		bool __fastcall GetPowerS1(BYTE Address, POWER * PowerS, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ������ �������� S(�� - ����� �����). POWER3PHASE
		bool __fastcall GetPowerS2(BYTE Address, POWER * PowerS, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ������ �������� S(�� - ����� �����). POWER3PHASE
		bool __fastcall GetPowerS3(BYTE Address, POWER * PowerS, ELECTROVAL * ElectroVal); //2.3.15.1 ����� ������� �� ������ ������ ������ �������� S(�� - ����� �����). POWER3PHASE
		bool __fastcall GetFrequency(BYTE Address, FREQUENCY * Frequency, ELECTROVAL * ElectroVal); //2.3.15.4 ����� ������� �� ������ ������ ������� FREQUENCY
		bool __fastcall GetDistortion1(BYTE Address, KOEFPHASEDISTORT * KDist, ELECTROVAL * ElectroVal); //2.3.15.5 ����� ������� �� ������ ������ ������������� ��������� ���������������� ������ ����������. KOEFPHASEDISTORT3PHASE
		bool __fastcall GetDistortion2(BYTE Address, KOEFPHASEDISTORT * KDist, ELECTROVAL * ElectroVal); //2.3.15.5 ����� ������� �� ������ ������ ������������� ��������� ���������������� ������ ����������. KOEFPHASEDISTORT3PHASE
		bool __fastcall GetDistortion3(BYTE Address, KOEFPHASEDISTORT * KDist, ELECTROVAL * ElectroVal); //2.3.15.5 ����� ������� �� ������ ������ ������������� ��������� ���������������� ������ ����������. KOEFPHASEDISTORT3PHASE

		bool __fastcall TestSearchMeter(BYTE Address);

		__property BYTE DefaultPASSWORD[int index] = {read = read_DefaultPassword, write = write_DefaultPassword};
		__property BYTE AccessLEVEL = {read = read_AccessLevel, write = write_AccessLevel};
		__property METERDATA MeterDATA[int index] = {read = read_MeterData};
};
#endif

