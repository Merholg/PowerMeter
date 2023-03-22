#ifndef POWERMETER_H
#define POWERMETER_H

#include <QDialog>
#include <QMap>
#include <QSpinBox>
#include <QAction>
#include "metervalue.h"

struct METERSET
{
    int Value;  // Значение  по умолчанию
    int MinLimit; // минимальное значение
    int MaxLimit; // максимальное значение
};

namespace Ui {
class PowerMeter;
}

class PowerMeter : public QDialog
{
    Q_OBJECT

public:
    explicit PowerMeter(QWidget *parent = nullptr);
    ~PowerMeter();

private slots:
    void on_actionDeviceDelete_triggered();
    void on_actionDeviceAdd_triggered();
    void on_spinMeterAddressFROM_valueChanged(int arg1);
    void RecvMeterSettings(QPair<QString, QString> arg1);
    void RecvEndMeterSettings();

public slots:
    void RecvMeterIniSettings();

signals:
    void SendMeterSection(QString arg1);
    void SendMeterSettings(QPair<QString, QString> arg1);


private:
    Ui::PowerMeter *ui;
    static const QMap<QString, METERSET> m_DeclMeterSettings;
    static const QString m_MeterGroupName;
    QMap<QString, QSpinBox *> m_ComboBoxes;
    QMap<int, DEVICEDATA> m_DeviceTable;
};

#endif // POWERMETER_H
