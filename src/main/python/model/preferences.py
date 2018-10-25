import glob
import os
from pathlib import Path

import matplotlib
import matplotlib.style as style
from qtpy.QtWidgets import QDialog, QFileDialog, QMessageBox

from ui.preferences import Ui_preferencesDialog

WINDOWS = ['barthann', 'bartlett', 'blackman', 'blackmanharris', 'bohman', 'boxcar', 'cosine', 'flattop', 'hamming',
           'hann', 'nuttall', 'parzen', 'triang', 'tukey']

SPECTROGRAM_FLAT = 'spectrogram (flat)'
SPECTROGRAM_CONTOURED = 'spectrogram (contoured)'
ELLIPSE = 'ellipse'
POINT = 'point'

SHOW_ALL_FILTERS = 'All'
SHOW_COMBINED_FILTER = 'Total'
SHOW_NO_FILTERS = 'None'
SHOW_FILTER_OPTIONS = [SHOW_ALL_FILTERS, SHOW_COMBINED_FILTER, SHOW_NO_FILTERS]

SHOW_ALL_SIGNALS = 'All'
SHOW_PEAK = 'Peak'
SHOW_AVERAGE = 'Average'
SHOW_SIGNAL_OPTIONS = [SHOW_ALL_SIGNALS, SHOW_PEAK, SHOW_AVERAGE]

SHOW_ALL_FILTERED_SIGNALS = 'All'
SHOW_FILTERED_ONLY = 'Filtered'
SHOW_UNFILTERED_ONLY = 'Unfiltered'
SHOW_FILTERED_SIGNAL_OPTIONS = [SHOW_ALL_FILTERED_SIGNALS, SHOW_FILTERED_ONLY, SHOW_UNFILTERED_ONLY]

EXTRACTION_OUTPUT_DIR = 'extraction/output_dir'
EXTRACTION_NOTIFICATION_SOUND = 'extraction/notification_sound'
EXTRACTION_BATCH_FILTER = 'extraction/batch_filter'
EXTRACTION_MIX_MONO = 'extraction/mix_to_mono'
EXTRACTION_DECIMATE = 'extraction/decimate'
EXTRACTION_INCLUDE_ORIGINAL = 'extraction/include_original'
EXTRACTION_COMPRESS = 'extraction/compress'

ANALYSIS_RESOLUTION = 'analysis/resolution'
ANALYSIS_TARGET_FS = 'analysis/target_fs'
ANALYSIS_WINDOW_DEFAULT = 'Default'
ANALYSIS_AVG_WINDOW = 'analysis/avg_window'
ANALYSIS_PEAK_WINDOW = 'analysis/peak_window'

AUDIO_ANALYSIS_MARKER_SIZE = 'audio/marker_size'
AUDIO_ANALYSIS_MARKER_TYPE = 'audio/marker_type'
AUDIO_ANALYSIS_ELLIPSE_WIDTH = 'audio/ellipse_width'
AUDIO_ANALYSIS_ELLIPSE_HEIGHT = 'audio/ellipse_height'
AUDIO_ANALYIS_MIN_FREQ = 'audio/min_freq'
AUDIO_ANALYIS_MAX_UNFILTERED_FREQ = 'audio/max_unfiltered_freq'
AUDIO_ANALYIS_MAX_FILTERED_FREQ = 'audio/max_filtered_freq'
AUDIO_ANALYSIS_COLOUR_MAX = 'audio/colour_max'
AUDIO_ANALYSIS_COLOUR_MIN = 'audio/colour_min'
AUDIO_ANALYSIS_SIGNAL_MIN = 'audio/signal_min'
AUDIO_ANALYSIS_GEOMETRY = 'audio/geometry'

BINARIES_GROUP = 'binaries'
BINARIES_FFPROBE = f"{BINARIES_GROUP}/ffprobe"
BINARIES_FFMPEG = f"{BINARIES_GROUP}/ffmpeg"

FILTERS_PRESET_x = 'filters/preset_%d'

SCREEN_GEOMETRY = 'screen/geometry'
SCREEN_WINDOW_STATE = 'screen/window_state'

STYLE_MATPLOTLIB_THEME_DEFAULT = 'default'
STYLE_MATPLOTLIB_THEME = 'style/matplotlib_theme'

DISPLAY_SHOW_LEGEND = 'display/show_legend'
DISPLAY_SHOW_FILTERS = 'display/show_filters'
DISPLAY_SHOW_SIGNALS = 'display/show_signals'
DISPLAY_SHOW_FILTERED_SIGNALS = 'display/show_filtered_signals'
DISPLAY_FREQ_STEP = 'display/freq_step'
DISPLAY_Q_STEP = 'display/q_step'
DISPLAY_S_STEP = 'display/s_step'
DISPLAY_GAIN_STEP = 'display/gain_step'
DISPLAY_LINE_STYLE = 'display/line_style'

GRAPH_X_AXIS_SCALE = 'graph/x_axis'
GRAPH_X_MIN = 'graph/x_min'
GRAPH_X_MAX = 'graph/x_max'

REPORT_GROUP = 'report'
REPORT_TITLE_FONT_SIZE = 'report/title_font_size'
REPORT_IMAGE_ALPHA = 'report/image/alpha'
REPORT_IMAGE_WIDTH = 'report/image/width'
REPORT_IMAGE_HEIGHT = 'report/image/height'
REPORT_FILTER_ROW_HEIGHT_MULTIPLIER = 'report/filter/row_height'
REPORT_FILTER_X0 = 'report/filter/x0'
REPORT_FILTER_X1 = 'report/filter/x1'
REPORT_FILTER_Y0 = 'report/filter/y0'
REPORT_FILTER_Y1 = 'report/filter/y1'
REPORT_FILTER_FONT_SIZE = 'report/filter/font_size'
REPORT_FILTER_SHOW_HEADER = 'report/filter/show_header'
REPORT_LAYOUT_MAJOR_RATIO = 'report/layout/major_ratio'
REPORT_LAYOUT_MINOR_RATIO = 'report/layout/minor_ratio'
REPORT_LAYOUT_SPLIT_DIRECTION = 'report/layout/split_direction'
REPORT_LAYOUT_WSPACE = 'report/layout/wspace'
REPORT_LAYOUT_HSPACE = 'report/layout/hspace'
REPORT_LAYOUT_TYPE = 'report/layout/type'
REPORT_CHART_GRID_ALPHA = 'report/chart/grid_alpha'
REPORT_CHART_SHOW_LEGEND = 'report/chart/show_legend'
REPORT_CHART_LIMITS_X0 = 'report/chart/limits_x0'
REPORT_CHART_LIMITS_X1 = 'report/chart/limits_x1'
REPORT_CHART_LIMITS_Y0 = 'report/chart/limits_y0'
REPORT_CHART_LIMITS_Y1 = 'report/chart/limits_y1'
REPORT_CHART_LIMITS_X_SCALE = 'report/chart/limits_x_scale'
REPORT_GEOMETRY = 'report/geometry'

LOGGING_LEVEL = 'logging/level'

SYSTEM_CHECK_FOR_UPDATES = 'system/check_for_updates'

DEFAULT_PREFS = {
    ANALYSIS_RESOLUTION: 1.0,
    ANALYSIS_TARGET_FS: 1000,
    ANALYSIS_AVG_WINDOW: ANALYSIS_WINDOW_DEFAULT,
    ANALYSIS_PEAK_WINDOW: ANALYSIS_WINDOW_DEFAULT,
    AUDIO_ANALYSIS_MARKER_SIZE: 1,
    AUDIO_ANALYSIS_MARKER_TYPE: POINT,
    AUDIO_ANALYSIS_ELLIPSE_WIDTH: 3.0,
    AUDIO_ANALYSIS_ELLIPSE_HEIGHT: 1.0,
    AUDIO_ANALYIS_MIN_FREQ: 1,
    AUDIO_ANALYIS_MAX_UNFILTERED_FREQ: 160,
    AUDIO_ANALYIS_MAX_FILTERED_FREQ: 40,
    AUDIO_ANALYSIS_COLOUR_MAX: -10,
    AUDIO_ANALYSIS_COLOUR_MIN: -70,
    AUDIO_ANALYSIS_SIGNAL_MIN: -70.0,
    STYLE_MATPLOTLIB_THEME: STYLE_MATPLOTLIB_THEME_DEFAULT,
    DISPLAY_SHOW_LEGEND: True,
    DISPLAY_SHOW_FILTERS: SHOW_ALL_FILTERS,
    EXTRACTION_OUTPUT_DIR: os.path.expanduser('~'),
    EXTRACTION_MIX_MONO: False,
    EXTRACTION_COMPRESS: False,
    EXTRACTION_DECIMATE: False,
    EXTRACTION_INCLUDE_ORIGINAL: False,
    DISPLAY_FREQ_STEP: '1',
    DISPLAY_Q_STEP: '0.1',
    DISPLAY_S_STEP: '0.1',
    DISPLAY_GAIN_STEP: '0.1',
    DISPLAY_LINE_STYLE: True,
    GRAPH_X_AXIS_SCALE: 'log',
    GRAPH_X_MIN: 1,
    GRAPH_X_MAX: 160,
    REPORT_FILTER_ROW_HEIGHT_MULTIPLIER: 1.2,
    REPORT_TITLE_FONT_SIZE: 36,
    REPORT_IMAGE_ALPHA: 1.0,
    REPORT_FILTER_X0: 0.748,
    REPORT_FILTER_X1: 1.0,
    REPORT_FILTER_Y0: 0.75,
    REPORT_FILTER_Y1: 1.0,
    REPORT_LAYOUT_MAJOR_RATIO: 1.0,
    REPORT_LAYOUT_MINOR_RATIO: 2.0,
    REPORT_LAYOUT_SPLIT_DIRECTION: 'Vertical',
    REPORT_LAYOUT_TYPE: 'Image | Chart',
    REPORT_CHART_GRID_ALPHA: 0.5,
    REPORT_CHART_SHOW_LEGEND: False,
    REPORT_CHART_LIMITS_X0: 1,
    REPORT_CHART_LIMITS_X1: 160,
    REPORT_CHART_LIMITS_X_SCALE: 'linear',
    REPORT_FILTER_SHOW_HEADER: True,
    REPORT_FILTER_FONT_SIZE: matplotlib.rcParams['font.size'],
    REPORT_LAYOUT_HSPACE: matplotlib.rcParams['figure.subplot.hspace'],
    REPORT_LAYOUT_WSPACE: matplotlib.rcParams['figure.subplot.wspace'],
    SYSTEM_CHECK_FOR_UPDATES: True
}

TYPES = {
    DISPLAY_SHOW_LEGEND: bool,
    DISPLAY_LINE_STYLE: bool,
    ANALYSIS_RESOLUTION: float,
    ANALYSIS_TARGET_FS: int,
    AUDIO_ANALYSIS_MARKER_SIZE: int,
    AUDIO_ANALYSIS_ELLIPSE_WIDTH: float,
    AUDIO_ANALYSIS_ELLIPSE_HEIGHT: float,
    AUDIO_ANALYIS_MIN_FREQ: int,
    AUDIO_ANALYIS_MAX_UNFILTERED_FREQ: int,
    AUDIO_ANALYIS_MAX_FILTERED_FREQ: int,
    AUDIO_ANALYSIS_COLOUR_MAX: int,
    AUDIO_ANALYSIS_COLOUR_MIN: int,
    AUDIO_ANALYSIS_SIGNAL_MIN: float,
    EXTRACTION_MIX_MONO: bool,
    EXTRACTION_COMPRESS: bool,
    EXTRACTION_DECIMATE: bool,
    EXTRACTION_INCLUDE_ORIGINAL: bool,
    GRAPH_X_MIN: int,
    GRAPH_X_MAX: int,
    REPORT_FILTER_ROW_HEIGHT_MULTIPLIER: float,
    REPORT_TITLE_FONT_SIZE: int,
    REPORT_IMAGE_ALPHA: float,
    REPORT_FILTER_X0: float,
    REPORT_FILTER_X1: float,
    REPORT_FILTER_Y0: float,
    REPORT_FILTER_Y1: float,
    REPORT_LAYOUT_MAJOR_RATIO: float,
    REPORT_LAYOUT_MINOR_RATIO: float,
    REPORT_LAYOUT_HSPACE: float,
    REPORT_LAYOUT_WSPACE: float,
    REPORT_CHART_GRID_ALPHA: float,
    REPORT_CHART_SHOW_LEGEND: bool,
    REPORT_CHART_LIMITS_X0: int,
    REPORT_CHART_LIMITS_X1: int,
    REPORT_FILTER_SHOW_HEADER: bool,
    REPORT_FILTER_FONT_SIZE: int,
    SYSTEM_CHECK_FOR_UPDATES: bool
}

COLOUR_INTERVALS = [x / 255 for x in range(36, 250, 24)] + [1.0]
# keep peak green, avg red and filters cyan
AVG_SPECLAB_COLOURS = [(x, 0.0, 0.0) for x in COLOUR_INTERVALS[::-1]]
PEAK_SPECLAB_COLOURS = [(0.0, x, 0.0) for x in COLOUR_INTERVALS[::-1]]
FILTER_COLOURS = [(0.0, x, x) for x in COLOUR_INTERVALS[::-1]]

singleton = None


def get_avg_colour(idx):
    if singleton is None or singleton.get(DISPLAY_LINE_STYLE) is True:
        return AVG_SPECLAB_COLOURS[idx % len(AVG_SPECLAB_COLOURS)]
    else:
        colours = matplotlib.rcParams['axes.prop_cycle'].by_key()['color']
        return colours[idx % len(colours)]


def get_peak_colour(idx):
    if singleton is None or singleton.get(DISPLAY_LINE_STYLE) is True:
        return PEAK_SPECLAB_COLOURS[idx % len(PEAK_SPECLAB_COLOURS)]
    else:
        colours = matplotlib.rcParams['axes.prop_cycle'].by_key()['color']
        return colours[idx % len(colours)]


def get_filter_colour(idx):
    return FILTER_COLOURS[idx % len(FILTER_COLOURS)]


class Preferences:
    def __init__(self, settings):
        self.__settings = settings
        global singleton
        singleton = self

    def has(self, key):
        '''
        checks for existence of a value.
        :param key: the key.
        :return: True if we have a value.
        '''
        return self.get(key) is not None

    def get(self, key, default_if_unset=True):
        '''
        Gets the value, if any.
        :param key: the settings key.
        :param default_if_unset: if true, return a default value.
        :return: the value.
        '''
        default_value = DEFAULT_PREFS.get(key, None) if default_if_unset is True else None
        value_type = TYPES.get(key, None)
        if value_type is not None:
            return self.__settings.value(key, defaultValue=default_value, type=value_type)
        else:
            return self.__settings.value(key, defaultValue=default_value)

    def get_all(self, prefix):
        '''
        Get all values with the given prefix.
        :param prefix: the prefix.
        :return: the values, if any.
        '''
        self.__settings.beginGroup(prefix)
        try:
            return set(filter(None.__ne__, [self.__settings.value(x) for x in self.__settings.childKeys()]))
        finally:
            self.__settings.endGroup()

    def set(self, key, value):
        '''
        sets a new value.
        :param key: the key.
        :param value:  the value.
        '''
        if value is None:
            self.__settings.remove(key)
        else:
            self.__settings.setValue(key, value)

    def clear_all(self, prefix):
        ''' clears all under the given group '''
        self.__settings.beginGroup(prefix)
        self.__settings.remove('')
        self.__settings.endGroup()

    def clear(self, key):
        '''
        Removes the stored value.
        :param key: the key.
        '''
        self.set(key, None)


class PreferencesDialog(QDialog, Ui_preferencesDialog):
    '''
    Allows user to set some basic preferences.
    '''

    def __init__(self, preferences, style_root, main_chart_limits, parent=None):
        super(PreferencesDialog, self).__init__(parent)
        self.__style_root = style_root
        self.setupUi(self)
        self.__init_analysis_window(self.avgAnalysisWindow)
        self.__init_analysis_window(self.peakAnalysisWindow)
        self.__init_themes()
        self.__preferences = preferences
        self.__main_chart_limits = main_chart_limits

        ffmpegLoc = self.__preferences.get(BINARIES_FFMPEG)
        if ffmpegLoc:
            if os.path.isdir(ffmpegLoc):
                self.ffmpegDirectory.setText(ffmpegLoc)

        ffprobeLoc = self.__preferences.get(BINARIES_FFPROBE)
        if ffprobeLoc:
            if os.path.isdir(ffprobeLoc):
                self.ffprobeDirectory.setText(ffprobeLoc)

        notifySoundLoc = self.__preferences.get(EXTRACTION_NOTIFICATION_SOUND)
        if notifySoundLoc:
            if os.path.isfile(notifySoundLoc):
                self.extractCompleteAudioFile.setText(notifySoundLoc)

        self.init_combo(ANALYSIS_TARGET_FS, self.targetFs,
                        translater=lambda a: 'Full Range' if a == 0 else str(a) + ' Hz')
        self.init_combo(ANALYSIS_RESOLUTION, self.resolutionSelect, translater=lambda a: str(a) + ' Hz')
        self.init_combo(ANALYSIS_AVG_WINDOW, self.avgAnalysisWindow)
        self.init_combo(ANALYSIS_PEAK_WINDOW, self.peakAnalysisWindow)
        self.init_combo(STYLE_MATPLOTLIB_THEME, self.themePicker)

        outputDir = self.__preferences.get(EXTRACTION_OUTPUT_DIR)
        if outputDir:
            if os.path.isdir(outputDir):
                self.defaultOutputDirectory.setText(outputDir)

        freq_is_log = self.__preferences.get(GRAPH_X_AXIS_SCALE)
        self.freqIsLogScale.setChecked(freq_is_log == 'log')
        self.xmin.setValue(self.__preferences.get(GRAPH_X_MIN))
        self.xmax.setValue(self.__preferences.get(GRAPH_X_MAX))

        self.speclabLineStyle.setChecked(self.__preferences.get(DISPLAY_LINE_STYLE))
        self.checkForUpdates.setChecked(self.__preferences.get(SYSTEM_CHECK_FOR_UPDATES))

        self.monoMix.setChecked(self.__preferences.get(EXTRACTION_MIX_MONO))
        self.decimate.setChecked(self.__preferences.get(EXTRACTION_DECIMATE))
        self.includeOriginal.setChecked(self.__preferences.get(EXTRACTION_INCLUDE_ORIGINAL))
        self.compress.setChecked(self.__preferences.get(EXTRACTION_COMPRESS))

    def __init_themes(self):
        '''
        Adds all the available matplotlib theme names to a combo along with our internal theme names.
        '''
        for p in glob.iglob(f"{self.__style_root}/style/mpl/*.mplstyle"):
            self.themePicker.addItem(Path(p).resolve().stem)
        for style_name in sorted(style.library.keys()):
            self.themePicker.addItem(style_name)

    def __init_analysis_window(self, combo):
        '''
        Adds the supported windows to the combo.
        :param combo: the combo.
        '''
        combo.addItem(ANALYSIS_WINDOW_DEFAULT)
        for w in WINDOWS:
            combo.addItem(w)

    def init_combo(self, key, combo, translater=lambda a: a):
        '''
        Initialises a combo box from either settings or a default value.
        :param key: the settings key.
        :param combo: the combo box.
        :param translater: a lambda to translate from the stored value to the display name.
        '''
        stored_value = self.__preferences.get(key)
        idx = -1
        if stored_value is not None:
            idx = combo.findText(translater(stored_value))
        if idx != -1:
            combo.setCurrentIndex(idx)

    def accept(self):
        '''
        Saves the locations if they exist.
        '''
        ffmpegLoc = self.ffmpegDirectory.text()
        if os.path.isdir(ffmpegLoc):
            self.__preferences.set(BINARIES_FFMPEG, ffmpegLoc)
        ffprobeLoc = self.ffprobeDirectory.text()
        if os.path.isdir(ffprobeLoc):
            self.__preferences.set(BINARIES_FFPROBE, ffprobeLoc)
        outputDir = self.defaultOutputDirectory.text()
        if os.path.isdir(outputDir):
            self.__preferences.set(EXTRACTION_OUTPUT_DIR, outputDir)
        notifySound = self.extractCompleteAudioFile.text()
        if len(notifySound) > 0 and os.path.isfile(notifySound):
            self.__preferences.set(EXTRACTION_NOTIFICATION_SOUND, notifySound)
        else:
            self.__preferences.set(EXTRACTION_NOTIFICATION_SOUND, None)
        text = self.targetFs.currentText()
        if text == 'Full Range':
            self.__preferences.set(ANALYSIS_TARGET_FS, 0)
        else:
            self.__preferences.set(ANALYSIS_TARGET_FS, int(text.split(' ')[0]))
        self.__preferences.set(ANALYSIS_RESOLUTION, float(self.resolutionSelect.currentText().split(' ')[0]))
        self.__preferences.set(ANALYSIS_AVG_WINDOW, self.avgAnalysisWindow.currentText())
        self.__preferences.set(ANALYSIS_PEAK_WINDOW, self.peakAnalysisWindow.currentText())
        current_theme = self.__preferences.get(STYLE_MATPLOTLIB_THEME)
        if current_theme is not None and current_theme != self.themePicker.currentText():
            self.alert_on_change('Theme Change')
        self.__preferences.set(STYLE_MATPLOTLIB_THEME, self.themePicker.currentText())
        new_x_scale = 'log' if self.freqIsLogScale.isChecked() else 'linear'
        update_limits = False
        if self.__preferences.get(GRAPH_X_AXIS_SCALE) != new_x_scale:
            update_limits = True
        self.__preferences.set(GRAPH_X_AXIS_SCALE, new_x_scale)
        if self.xmin.value() < self.xmax.value():
            if self.__preferences.get(GRAPH_X_MIN) != self.xmin.value():
                update_limits = True
                self.__preferences.set(GRAPH_X_MIN, self.xmin.value())
            if self.__preferences.get(GRAPH_X_MAX) != self.xmax.value():
                update_limits = True
                self.__preferences.set(GRAPH_X_MAX, self.xmax.value())
        else:
            self.alert_on_change('X Axis Invalid', text='Invalid values: x_min must be less than x_max',
                                 icon=QMessageBox.Critical)
        if update_limits:
            self.__main_chart_limits.update(x_min=self.xmin.value(), x_max=self.xmax.value(),
                                            x_scale=new_x_scale, draw=True)
        self.__preferences.set(SYSTEM_CHECK_FOR_UPDATES, self.checkForUpdates.isChecked())
        self.__preferences.set(DISPLAY_LINE_STYLE, self.speclabLineStyle.isChecked())
        self.__preferences.set(EXTRACTION_MIX_MONO, self.monoMix.isChecked())
        self.__preferences.set(EXTRACTION_DECIMATE, self.decimate.isChecked())
        self.__preferences.set(EXTRACTION_INCLUDE_ORIGINAL, self.includeOriginal.isChecked())
        self.__preferences.set(EXTRACTION_COMPRESS, self.compress.isChecked())
        QDialog.accept(self)

    def alert_on_change(self, title, text='Change will not take effect until the application is restarted',
                        icon=QMessageBox.Warning):
        msg_box = QMessageBox()
        msg_box.setText(text)
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.exec()

    def __get_directory(self, name):
        dialog = QFileDialog(parent=self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(f"{name}.exe")
        dialog.setWindowTitle(f"Select {name}.exe")
        if dialog.exec():
            selected = dialog.selectedFiles()
            if len(selected) > 0:
                return selected[0]
        return None

    def showFfmpegDirectoryPicker(self):
        loc = self.__get_directory('ffmpeg')
        if loc is not None:
            dirname = os.path.dirname(loc)
            self.ffmpegDirectory.setText(dirname)
            if os.path.exists(os.path.join(dirname, 'ffprobe.exe')):
                self.ffprobeDirectory.setText(dirname)

    def showFfprobeDirectoryPicker(self):
        loc = self.__get_directory('ffprobe')
        if loc is not None:
            dirname = os.path.dirname(loc)
            self.ffprobeDirectory.setText(dirname)
            if os.path.exists(os.path.join(dirname, 'ffmpeg.exe')):
                self.ffmpegDirectory.setText(dirname)

    def showDefaultOutputDirectoryPicker(self):
        dialog = QFileDialog(parent=self)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setWindowTitle(f"Select Extract Audio Output Directory")
        if dialog.exec():
            selected = dialog.selectedFiles()
            if len(selected) > 0:
                self.defaultOutputDirectory.setText(selected[0])

    def showExtractCompleteSoundPicker(self):
        dialog = QFileDialog(parent=self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Audio (*.wav)")
        dialog.setWindowTitle(f"Select Notification Sound")
        if dialog.exec():
            selected = dialog.selectedFiles()
            if len(selected) > 0:
                self.extractCompleteAudioFile.setText(selected[0])
            else:
                self.extractCompleteAudioFile.setText('')
        else:
            self.extractCompleteAudioFile.setText('')
