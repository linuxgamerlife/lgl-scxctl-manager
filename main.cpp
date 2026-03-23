#include <QApplication>
#include <QIcon>
#include "mainwindow.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    app.setApplicationName("SCX Scheduler Manager");
    app.setApplicationVersion("1.0.0");
    app.setOrganizationName("scx-scheduler-manager");

    app.setWindowIcon(QIcon(":/icons/scxctl-manager_icon.png"));

    MainWindow w;
    w.show();
    return app.exec();
}
