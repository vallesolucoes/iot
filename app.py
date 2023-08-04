import streamlit as st
import serial.tools.list_ports
import threading

# Variáveis globais para controle da leitura serial
ser = None
reading = False
reading_thread = None
data_buffer = ""

def main():
    st.title("Comunicação Serial e Formulário com Streamlit")

    # Dividir a tela em duas colunas
    col1, col2 = st.columns(2)

    # Widgets de comunicação serial na coluna 1
    with col1:
        st.markdown("## Comunicação Serial")
        # Listar todas as portas seriais disponíveis
        serial_ports = [port.device for port in serial.tools.list_ports.comports()]
        # Criar um campo de seleção para as portas seriais
        selected_port = st.selectbox("Porta Serial", serial_ports)
        # Campo para o baudrate
        baud_rate = st.number_input("Baudrate", min_value=1, value=9600, step=1)

        # Botão para abrir a porta serial automaticamente
        if st.button("Abrir Porta Serial"):
            global ser, reading
            try:
                ser = serial.Serial(selected_port, baud_rate)
                reading = True
                start_serial_thread()  # Iniciar a thread de leitura
            except serial.SerialException as e:
                st.error(f"Erro ao abrir a porta serial: {e}")

    # Formulário na coluna 2
    with col2:
        st.markdown("## Formulário")
        # Campos de entrada de usuário
        name = st.text_input("Nome", "")
        email = st.text_input("Email", "")
        age = st.number_input("Idade", min_value=0, max_value=150, value=0, step=1)

        # Botão para enviar o formulário
        if st.button("Enviar"):
            # Exibindo os dados inseridos pelo usuário
            st.write("Nome:", name)
            st.write("Email:", email)
            st.write("Idade:", age)

    # Elemento para exibir os dados recebidos pela serial em tempo real (terminal do linux)
    st.markdown("## Dados Recebidos pela Serial")
    data_display = st.empty()

    while True:
        if reading and ser is not None:
            try:
                serial_data = ser.read().decode('utf-8')
                data_buffer += serial_data
                # Limitar o buffer de dados para evitar sobrecarga de memória
                if len(data_buffer) > 10000:
                    data_buffer = data_buffer[-10000:]
                data_display.text(data_buffer)
            except:
                pass

def start_serial_thread():
    global reading_thread, data_buffer
    data_buffer = ""
    reading_thread = threading.Thread(target=read_serial_data)
    reading_thread.start()

if __name__ == "__main__":
    main()
