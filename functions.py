def open_close_frame(botao, states):
        if states[botao.name][1] == "reduced":
            m_frame = states[botao.name][0]
            m_frame.configure(width=1400)
            states[botao.name][1] = "expanded"
            for i in states:
                if states[i][0] != m_frame and states[i][1] == "expanded":
                    states[i][0].configure(width=1)
                    states[i][1] = "reduced"
                else:
                    pass
        elif states[botao.name][1] == "expanded":
            m_frame = states[botao.name][0]
            m_frame.configure(width=1)
            states[botao.name][1] = "reduced"