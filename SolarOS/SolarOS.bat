@echo off
setlocal enabledelayedexpansion
:SET_CONFIG
set "os_version=2.0"
set "current_theme=60"
set "senha_sistema=solar123"

:LOGIN
title SolarOS %os_version% - Login
color 0E
cls
echo =========================================
echo             SOLAR OS - LOGIN
echo =========================================
echo Senha: solar123
echo.
set /p "pass=Digite a Senha: "
if "%pass%"=="%senha_sistema%" goto DESKTOP
echo Senha incorreta!
pause
goto LOGIN

:DESKTOP
title SolarOS %os_version% - Desktop
color %current_theme%
cls
echo ==========================================================
echo   SolarOS %os_version%   ^|   Data: %date%   ^|   %time%
echo ==========================================================
echo   1. [CAL] Calendario      2. [CLOCK] Relogio 
echo   3. [NOTE] Bloco de Notas 4. [THEME] Mudar Tema
echo   5. [CMD]  Solar Prompt   6. [EXIT]  Sair
echo ----------------------------------------------------------
echo.
set /p "choice=O que deseja abrir? (Digite o numero ou nome): "

if "%choice%"=="1" goto CALENDAR
if /i "%choice%"=="cal" goto CALENDAR
if "%choice%"=="2" goto CLOCK
if /i "%choice%"=="clock" goto CLOCK
if "%choice%"=="3" goto FLARE
if /i "%choice%"=="note" goto FLARE
if "%choice%"=="4" goto THEMES
if /i "%choice%"=="theme" goto THEMES
if "%choice%"=="5" goto PROMPT
if /i "%choice%"=="cmd" goto PROMPT
if "%choice%"=="6" exit
if /i "%choice%"=="exit" exit

echo Opcao invalida!
timeout /t 2 >nul
goto DESKTOP

:CALENDAR
cls
echo --- CALENDARIO SOLAR ---
echo.
net helpmsg 60 >nul 2>&1 && (powershell -command "Get-Date | format-table") || (date /t)
echo.
echo Pressione qualquer tecla para voltar ao Desktop.
pause >nul
goto DESKTOP

:CLOCK
cls
echo --- RELOGIO DO SISTEMA ---
echo.
echo A hora atual e: %time%
echo.
echo [1] Atualizar  [2] Voltar
set /p "clk=Opcao: "
if "%clk%"=="1" goto CLOCK
goto DESKTOP

:FLARE
cls
echo --- FLARE NOTEBOOK ---
echo Digite o nome do arquivo (ex: notas.txt):
set /p "filename=>> "
echo Digite o texto (Ao terminar, a janela fechara para salvar):
notepad "%filename%"
echo Arquivo %filename% processado.
pause
goto DESKTOP

:THEMES
cls
echo --- TEMAS DO SOLAR OS ---
echo 1. Solar (Padrao)
echo 2. Eclipse (Escuro)
echo 3. Neon (Verde)
echo 4. Oceano (Azul)
set /p "t_choice=Escolha o tema: "
if "%t_choice%"=="1" set "current_theme=60"
if "%t_choice%"=="2" set "current_theme=0F"
if "%t_choice%"=="3" set "current_theme=0A"
if "%t_choice%"=="4" set "current_theme=1F"
goto DESKTOP

:PROMPT
cls
color 07
echo --- SOLAR PROMPT (Digite 'exit' para voltar ao desktop) ---
:P_LOOP
set /p "scmd=SolarOS\CMD> "
if /i "%scmd%"=="exit" goto DESKTOP
%scmd%
goto P_LOOP