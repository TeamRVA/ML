import gradio as gr
import subprocess as sub
import soundfile as sf
from pydub import AudioSegment as AS
def change(vocal, instrument, voice, record, name):
    output_path = f'/home/modeep3/Desktop/DDSP-SVC/outputs/{name}.mp3'

    if record != None:
        r, data = record
        input_path = f'/home/modeep3/Desktop/DDSP-SVC/inputs/{name}.mp3'
        sf.write(input_path, data, r)
        cmd = ['python', 'main.py', '-i', f'{input_path}', '-m', f'/home/modeep3/Desktop/DDSP-SVC/exp/combsub-test/{voice}.pt', '-o', f'{output_path}']
    else:
        cmd = ['python', 'main.py', '-i', f'{vocal}', '-m', f'/home/modeep3/Desktop/DDSP-SVC/exp/combsub-test/{voice}.pt', '-o', f'{output_path}']

    if voice == 'YooChanhong':
        if instrument == None:
            sub.run(cmd)
            return output_path, f'Uploaded voice converted successfully -> "{voice}"'
        else:
            sub.run(cmd)
            a = AS.from_file(output_path)
            r = a.overlay(AS.from_file(instrument))
            r.export(output_path, format='mp3')
            return output_path, f'Uploaded voice and instruments converted successfully -> "{voice}"'
        
    elif voice == 'FlutterDeveloper':
        if instrument == None:
            sub.run(cmd)
            return output_path, f'Uploaded voice converted successfully -> "{voice}"'
        else:
            sub.run(cmd)
            a = AS.from_file(output_path)
            r = a.overlay(AS.from_file(instrument))
            r.export(output_path, format='mp3')
            return output_path, f'Uploaded voice and instruments converted successfully -> "{voice}"'
            

demo = gr.Interface(
    change,
    inputs=[
        gr.Audio(type='filepath', label='Upload Voice File'),
        gr.Audio(type='filepath', label='Upload Music File (if you want)'),
        gr.Radio(["YooChanhong", "FlutterDeveloper"], label='Voice List', info='What do you want to use?'),
        gr.Microphone(source="microphone", type="numpy"),
        gr.Textbox(label='Name the song')
    ],
    outputs=[
        gr.Audio(label='Changed Voice File'),
        gr.Textbox(label='Results')
    ],
    title='RVA voice changer (BETA)',
    description='Made by MoDeep',
    theme=gr.themes.Soft()
).launch()