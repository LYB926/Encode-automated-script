import os

def generate(bitratek, rawName, rawFrames):
    rawPath      = '/data/CAOYUE/MSU2021/'
    # bitratek     = input('Output bitrate  : ')
    bitrate      = str(int(bitratek)*1000)    
    rawNameSplit = rawName.split('.')           #Result: ['apple_tree_1920x1080_30', 'yuv']
    tempSplit    = rawNameSplit[0].split('_')   #Result: ['apple', 'tree', '1920x1080', '30']
    for w in tempSplit:         # rawResolution
        if w == '1920x1080':
            rawResolution = w
        elif w == '1440x1080':
            rawResolution = w
    rawWidth  = (rawResolution.split('x'))[0]
    rawHeight = (rawResolution.split('x'))[1]
    # outFrameRate  = input('Output framerate  : ')
    outputPath = '/data/WispChan/jm_benchmark_output/'+rawNameSplit[0]+'/'

    for w in tempSplit:         # rawFrameRate
        if w == '30':
            rawFrameRate = w + '.0'
        elif w == '52':
            rawFrameRate = w + '.0'
        elif w == '25':
            rawFrameRate = w + '.0'
        elif w == '24':
            rawFrameRate = w + '.0'
        elif w == '60':
            rawFrameRate = w + '.0'
        elif w == '39':
            rawFrameRate = w + '.0'
        elif w == '50':
            rawFrameRate = w + '.0'

    fileName = rawNameSplit[0] + '_' + bitratek + '.cfg'
    file = open(fileName, mode='w', encoding='utf-8')

    cfg1 = \
    '''##########################################################################################
    # Files
    ##########################################################################################
    '''
    file.write(cfg1)
    file.write('InputFile             = \"' + rawPath + rawName + '\"')

    cfg2 = \
    '''
    InputHeaderLength     = 0      # If the inputfile has a header, state it's length in byte here
    StartFrame            = 0      # Start frame for encoding. (0-N)
    '''
    file.write(cfg2)
    para1 = 'FramesToBeEncoded     = ' + rawFrames + '     # Number of frames to be coded\n'
    para2 = '    FrameRate             = ' + rawFrameRate + '  # Frame Rate per second (0.1-100.0)'
    file.write(para1 + para2)

    cfg3 = '''Enable32Pulldown      = 0      # Enable 'hard' 3:2 pulldown (modifying the inpur data)
                                # 0 = disabled
                                # 1 = A, B, Bt|Cb, Ct|Db, D
                                # 2 = A, B, C, Ct|Db, D
    SEIVUI32Pulldown      = 0      # Enable 3:2 pulldown through VUI and SEI metadata signaling. Five methods are supported:
                                # 0 = disabled
                                # 1 = A, Bt|Bb, Bt|Cb, Ct|Cb, D
                                # 2 = A, B, C, C, D
                                # 3 = At|Ab, Bt|Bb, Bt|Cb, Ct|Cb, Dt|Db
                                # 4 = A, Bt|Bb, Bt|Cb, Ct|Db, Dt|Db
                                # 5 = At|Ab, Bt|Bb, Bt|Cb, Ct|Db, Dt|Db
    '''
    file.write(cfg3)

    para3 = 'SourceWidth           = ' + rawWidth + '    # Source frame width\n    SourceHeight          = ' + rawHeight + '    # Source frame height\n    SourceResize          = 0       # Resize source size for output\n    OutputWidth           = ' + rawWidth + '    # Output frame width\n    OutputHeight          = ' + rawHeight + '    # Output frame height'
    file.write(para3)

    cfg4 = '''
    ProcessInput          = 0      # Filter Input Sequence 
    Interleaved           = 0      # 0: Planar input, 1: Packed input
    PixelFormat           = 0      # Pixel Format for 422 packed inputs
                                # 0: UYVY
                                # 1: YUY2/YUYV
                                # 2: YVYU
                                # 3: BGR (Unsupported)
                                # 4: V210 (Video Clarity)

    StandardRange         = 0      # 0: Standard range 1: Full range (RGB input)
    VideoCode             = 1      # Video codes for RGB ==> YUV conversions
                                # 0 = NULL,
                                # 1 = ITU_REC709,
                                # 2 = CCIR_601,
                                # 3 = FCC,
                                # 4 = ITU_REC624BG,
                                # 5 = SMPTE_170M,
                                # 6 = SMPTE_240M,
                                # 7 = SMPTE_260M,
                                # 8 = ITU_REC709_EXACT

    TraceFile             = "trace_enc.txt"      # Trace file 
    ReconFile             = "test_rec.yuv"       # Reconstruction YUV file
    '''
    file.write(cfg4)

    file.write('OutputFile            = "' + outputPath + rawNameSplit[0] + '_' + bitratek + '.264' + '"           # Bitstream\n    ')
    cfg5 = '''StatsFile             = "stats.dat"          # Coding statistics file

    NumberOfViews         = 1                     # Number of views to encode (1=1 view, 2=2 views)
    View1ConfigFile       = "encoder_view1.cfg"   # Config file name for second view
    ##########################################################################################
    # Encoder Control
    ##########################################################################################
    Grayscale             = 0   # Encode in grayscale (Currently only works for 8 bit YUV 420 input)
    ProfileIDC            = 100 # Profile IDC (66=baseline, 77=main, 88=extended; FREXT Profiles: 100=High, 110=High 10, 122=High 4:2:2, 244=High 4:4:4, 44=CAVLC 4:4:4 Intra, 118=Multiview High Profile, 128=Stereo High Profile)
    IntraProfile          = 0   # Activate Intra Profile for FRExt (0: false, 1: true)
                                # (e.g. ProfileIDC=110, IntraProfile=1  =>  High 10 Intra Profile)
    LevelIDC              = 42  # Level IDC   (e.g. 20 = level 2.0)

    IntraPeriod           = 0   # Period of I-pictures   (0=only first)
    IDRPeriod             = 0   # Period of IDR pictures (0=only first)
    AdaptiveIntraPeriod   = 1   # Adaptive intra period
    AdaptiveIDRPeriod     = 0   # Adaptive IDR period
    IntraDelay            = 0   # Intra (IDR) picture delay (i.e. coding structure of PPIPPP... )
    EnableIDRGOP          = 0   # Support for IDR closed GOPs (0: disabled, 1: enabled)
    EnableOpenGOP         = 0   # Support for open GOPs (0: disabled, 1: enabled)
    QPISlice              = 28  # Quant. param for I Slices (0-51)
    QPPSlice              = 28  # Quant. param for P Slices (0-51)
    FrameSkip             = 0   # Number of frames to be skipped in input (e.g 2 will code every third frame). 
                                # Note that this now excludes intermediate (i.e. B) coded pictures
    ChromaQPOffset        = 0   # Chroma QP offset (-51..51)

    DisableSubpelME       = 0   # Disable Subpixel Motion Estimation (0=off/default, 1=on)
    SearchRange           = 32  # Max search range
    MESoftenSSEMetric     = 0   # soften lambda criterion for SSE ME
    MEDistortionFPel      = 0   # Select error metric for Full-Pel ME    (0: SAD, 1: SSE, 2: Hadamard SAD)
    MEDistortionHPel      = 2   # Select error metric for Half-Pel ME    (0: SAD, 1: SSE, 2: Hadamard SAD)
    MEDistortionQPel      = 2   # Select error metric for Quarter-Pel ME (0: SAD, 1: SSE, 2: Hadamard SAD)
    MDDistortion          = 2   # Select error metric for Mode Decision  (0: SAD, 1: SSE, 2: Hadamard SAD)
    SkipDeBlockNonRef     = 0   # Skip Deblocking (regardless of DFParametersFlag) for non-reference frames (0: off, 1: on)
    OnTheFlyFractMCP      = 0   # Perform on-the-fly fractional pixel interpolation for Motion Compensation and Motion Estimation
                                # 0: Disable, interpolate & store all positions
                                # 1: Store full pel & interpolated 1/2 pel positions; 1/4 pel positions interpolate on-the-fly
                                # 2: Store only full pell positions; 1/2 & 1/4 pel positions interpolate on-the-fly
    ChromaMCBuffer        = 1   # Calculate Color component interpolated values in advance and store them.
                                # Provides a trade-off between memory and computational complexity
                                # (0: disabled/default, 1: enabled)
    ChromaMEEnable        = 0   # Take into account Color component information during ME
                                # (0: only first component/default, 
                                #  1: All Color components - Integer refinement only
                                #  2: All Color components - All refinements)
    ChromaMEWeight        = 0   # Weighting for chroma components. This parameter should have a relationship with color format.

    NumberReferenceFrames = 4   # Number of previous frames used for inter motion search (0-16)

    PList0References      = 0   # P slice List 0 reference override (0 disable, N <= NumberReferenceFrames)
    Log2MaxFNumMinus4     = 0   # Sets log2_max_frame_num_minus4 (-1 : based on FramesToBeEncoded/Auto, >=0 : Log2MaxFNumMinus4)
    Log2MaxPOCLsbMinus4   = -1  # Sets log2_max_pic_order_cnt_lsb_minus4 (-1 : Auto, >=0 : Log2MaxPOCLsbMinus4)

    GenerateMultiplePPS   = 1   # Transmit multiple parameter sets. Currently parameters basically enable all WP modes (0: diabled, 1: enabled)
    SendAUD               = 0   # Send Access Delimiter Unit NALU (for every access unit)
    ResendSPS             = 2   # Resend SPS  (0: disabled, 1: all Intra pictures, 2: only for IDR, 3: for IDR and OpenGOP I)
    ResendPPS             = 0   # Resend PPS (with pic_parameter_set_id 0) for every coded Frame/Field pair (0: disabled, 1: enabled)

    MbLineIntraUpdate     = 0   # Error robustness(extra intra macro block updates)(0=off, N: One GOB every N frames are intra coded)
    RandomIntraMBRefresh  = 0   # Forced intra MBs per picture

    ##########################################################################################
    # PSlice Mode types
    ##########################################################################################
    PSliceSkip            = 1   # P-Slice Skip mode consideration  (0=disable, 1=enable)
    PSliceSearch16x16     = 1   # P-Slice Inter block search 16x16 (0=disable, 1=enable)
    PSliceSearch16x8      = 1   # P-Slice Inter block search 16x8  (0=disable, 1=enable)
    PSliceSearch8x16      = 1   # P-Slice Inter block search  8x16 (0=disable, 1=enable)
    PSliceSearch8x8       = 1   # P-Slice Inter block search  8x8  (0=disable, 1=enable)
    PSliceSearch8x4       = 1   # P-Slice Inter block search  8x4  (0=disable, 1=enable)
    PSliceSearch4x8       = 1   # P-Slice Inter block search  4x8  (0=disable, 1=enable)
    PSliceSearch4x4       = 1   # P-Slice Inter block search  4x4  (0=disable, 1=enable)

    ##########################################################################################
    # BSlice Mode types
    ##########################################################################################

    BSliceDirect          = 1   # B-Slice Skip mode consideration  (0=disable, 1=enable)
    BSliceSearch16x16     = 1   # B-Slice Inter block search 16x16 (0=disable, 1=enable)
    BSliceSearch16x8      = 1   # B-Slice Inter block search 16x8  (0=disable, 1=enable)
    BSliceSearch8x16      = 1   # B-Slice Inter block search  8x16 (0=disable, 1=enable)
    BSliceSearch8x8       = 1   # B-Slice Inter block search  8x8  (0=disable, 1=enable)
    BSliceSearch8x4       = 1   # B-Slice Inter block search  8x4  (0=disable, 1=enable)
    BSliceSearch4x8       = 1   # B-Slice Inter block search  4x8  (0=disable, 1=enable)
    BSliceSearch4x4       = 1   # B-Slice Inter block search  4x4  (0=disable, 1=enable)

    BiPredSearch16x16     = 1   # B-Slice Bi-prediction block search 16x16 (0=disable, 1=enable)
    BiPredSearch16x8      = 1   # B-Slice Bi-prediction block search 16x8  (0=disable, 1=enable)
    BiPredSearch8x16      = 1   # B-Slice Bi-prediction block search 8x16  (0=disable, 1=enable)
    BiPredSearch8x8       = 0   # B-Slice Bi-prediction block search 8x8   (0=disable, 1=enable)

    DisableIntra4x4        = 0  # Disable Intra 4x4 modes
    DisableIntra16x16      = 0  # Disable Intra 16x16 modes
    DisableIntraInInter    = 0  # Disable Intra modes for inter slices
    IntraDisableInterOnly  = 0  # Apply Disabling Intra conditions only to Inter Slices (0:disable/default,1: enable)
    Intra4x4ParDisable     = 0  # Disable Vertical & Horizontal 4x4
    Intra4x4DiagDisable    = 0  # Disable Diagonal 45degree 4x4
    Intra4x4DirDisable     = 0  # Disable Other Diagonal 4x4
    Intra16x16ParDisable   = 0  # Disable Vertical & Horizontal 16x16
    Intra16x16PlaneDisable = 0  # Disable Planar 16x16
    ChromaIntraDisable     = 0  # Disable Intra Chroma modes other than DC
    EnableIPCM             = 1  # Enable IPCM macroblock mode

    DisposableP            = 0  # Enable Disposable P slices in the primary layer (0: disable/default, 1: enable)
    DispPQPOffset          = 0  # Quantizer offset for disposable P slices (0: default)

    PreferDispOrder        = 1  # Prefer display order when building the prediction structure as opposed to coding order (affects intra and IDR periodic insertion, among others)
    PreferPowerOfTwo       = 0  # Prefer prediction structures that have lengths expressed as powers of two
    FrmStructBufferLength  = 16 # Length of the frame structure unit buffer; it can be overriden for certain cases

    ChangeQPFrame          = 0  # Frame in display order from which to apply the Change QP offsets
    ChangeQPI              = 0  # Change QP offset value for I_SLICE
    ChangeQPP              = 0  # Change QP offset value for P_SLICE
    ChangeQPB              = 0  # Change QP offset value for B_SLICE
    ChangeQPSI             = 0  # Change QP offset value for SI_SLICE
    ChangeQPSP             = 0  # Change QP offset value for SP_SLICE

    ##########################################################################################
    # B Slices
    ##########################################################################################

    NumberBFrames          = 7  # Number of B coded frames inserted (0=not used)
    PReplaceBSlice         = 0  # Replace B-coded slices with P-coded slices when NumberBFrames>0
    QPBSlice               = 30 # Quant. param for B slices (0-51)
    BRefPicQPOffset        = -1 # Quantization offset for reference B coded pictures (-51..51)
    DirectModeType         = 1  # Direct Mode Type (0:Temporal 1:Spatial)
    DirectInferenceFlag    = 1  # Direct Inference Flag (0: Disable 1: Enable)
    BList0References       = 0  # B slice List 0 reference override (0 disable, N <= NumberReferenceFrames)
    BList1References       = 1  # B slice List 1 reference override (0 disable, N <= NumberReferenceFrames)
                                # 1 List1 reference is usually recommended for normal GOP Structures.
                                # A larger value is usually more appropriate if a more flexible
                                # structure is used (i.e. using HierarchicalCoding)

    BReferencePictures    =  0  # Referenced B coded pictures (0=off, 1=B references for secondary layer, 2=B references for primary layer)

    HierarchicalCoding      =  3  # B hierarchical coding (0= off, 1= 2 layers, 2= 2 full hierarchy, 3 = explicit)
    HierarchyLevelQPEnable  =  1  # Adjust QP based on hierarchy level (in increments of 1). Overrides BRefPicQPOffset behavior.(0=off, 1=on)
    ExplicitHierarchyFormat = "b3r0b1r1b0e2b2e2b5r1b4e2b6e2" # Explicit Enhancement GOP. Format is {FrameDisplay_orderReferenceQP}.
                                                            # Valid values for reference type is r:reference, e:non reference.
    ExplicitSeqCoding     =  0    # Enable support for explicit sequence coding
    ExplicitSeqFile       =  "explicit_seq.cfg"
    LowDelay              =  0    # Apply HierarchicalCoding without delay (i.e., encode in the captured/display order)
    ReferenceReorder      =  1    # Reorder References according to Poc distance for HierarchicalCoding (0=off, 1=enable, 2=use when LowDelay is set)
    UseDistortionReorder  =  0    # Enable Distortion based reordering, when ReferenceReorder is set to 1
    PocMemoryManagement   =  1    # Memory management based on Poc Distances for HierarchicalCoding (0=off, 1=on, 2=use when LowDelay is set)
    SetFirstAsLongTerm    =  0    # Set first frame as long term

    BiPredMotionEstimation = 1   # Enable Bipredictive based Motion Estimation (0:disabled, 1:enabled)
    BiPredMERefinements    = 3   # Bipredictive ME extra refinements (0: single, N: N extra refinements (1 default)
    BiPredMESearchRange    = 16  # Bipredictive ME Search range (8 default). Note that range is halved for every extra refinement.
    BiPredMESubPel         = 2   # Bipredictive ME Subpixel Consideration (0: disabled, 1: single level, 2: dual level)

    ##########################################################################################
    # HM like coding structures
    ##########################################################################################

    BLevel0MoreRef        =  0  # 0: Use the same number of reference pictures as the other B pictures
                                # 1: Use more reference frame pictures for B pictures at level 0
    BIdenticalList        =  0  # 0: not used; 1: used for B pictures at level 0; 2: used for all B pictures
                                # 1 and 2 need to set ReferenceReorder to 1
    CRA                   =  0  # 0: do not use CRA like random access support; 1 use CRA like random access support
                                # only used for random access cases, LowDelay != 1
    HM50RefStructure      =  0  # 0: do not use HM-5.0 like referencing structure; 1 use HM-5.0 like referencing structure for random access
    LDRefSetting          =  0  # 0: use nearest pictures as reference frames
                                # 1: use one nearest + POC%4==0 pictures as reference frames, as JCTVC-F701
                                # Only low delay is supported, please do not use it for a different coding structure

    ##########################################################################################
    # SP Frames
    ##########################################################################################

    SPPicturePeriodicity  = 0                  # SP-Picture Periodicity (0=not used)
    SPSwitchPeriod        = 0                  # Switch period (in terms of switching SP/SI frames) between bitstream 1 and bitstream 2
    QPSPSlice             = 36                 # Quant. param of SP-Slices for Prediction Error (0-51)
    QPSISlice             = 36                 # Quant. param of SI-Slices for Prediction Error (0-51)
    QPSP2Slice            = 35                 # Quant. param of SP/SI-Slices for Predicted Blocks (0-51)
    SI_FRAMES             = 0                  # SI frame encoding flag (0=not used, 1=used)
    SP_output             = 0                  # Controls whether coefficients will be output to encode switching SP frames (0=no, 1=yes)
    SP_output_name        = "low_quality.dat"  # Filename for SP output coefficients
    SP2_FRAMES            = 0                  # switching SP frame encoding flag (0=not used, 1=used)
    SP2_input_name1       = "high_quality.dat" # Filename for the first swithed bitstream coefficients
    SP2_input_name2       = "low_quality.dat"  # Filename for the second switched bitstream coefficients

    ##########################################################################################
    # Output Control, NALs
    ##########################################################################################

    SymbolMode             =  1  # Symbol mode (Entropy coding method: 0=UVLC, 1=CABAC)
    OutFileMode            =  0  # Output file mode, 0:Annex B, 1:RTP
    PartitionMode          =  0  # Partition Mode, 0: no DP, 1: 3 Partitions per Slice

    ##########################################################################################
    # CABAC context initialization
    ##########################################################################################

    ContextInitMethod        =  1     # Context init (0: fixed, 1: adaptive)
    FixedModelNumber         =  0     # model number for fixed decision for inter slices ( 0, 1, or 2 )

    ##########################################################################################
    # Interlace Handling
    #########################################################################################

    PicInterlace             =  0     # Picture AFF    (0: frame coding, 1: field coding, 2:adaptive frame/field coding)
    MbInterlace              =  0     # Macroblock AFF (0: frame coding, 1: field coding, 2:adaptive frame/field coding, 3: frame MB-only AFF)
    IntraBottom              =  0     # Force Intra Bottom at GOP Period

    ##########################################################################################
    # Weighted Prediction
    #########################################################################################

    WeightedPrediction       =  0     # P picture Weighted Prediction (0=off, 1=explicit mode)
    WeightedBiprediction     =  0     # B picture Weighted Prediciton (0=off, 1=explicit mode,  2=implicit mode)
    ChromaWeightSupport      =  1     # Enable consideration of weights for Chroma components
    UseWeightedReferenceME   =  1     # Use weighted reference for ME (0=off, 1=on)
    WPMethod                 =  1     # WP method (0: DC based, 1: LMS based)
    WPIterMC                 =  0     # Iterative Motion compensated based weighted prediction method
    EnhancedBWeightSupport   =  0     # Enhanced B Weight support (needs revisit if we wish to merge with WPMethod)
    WPMCPrecision            =  0     # Improved Motion Compensation Precision using WP based methods.
                                    # Clones WP references with slightly modified rounding offsets (Requires RDPictureDecision and GenerateMultiplePPS) :
                                    # 0: disabled (default) 
                                    # 1: Up to one additional coding pass. Ref0 is 0, ref1 is 0 with a -1 offset
                                    # 2: Up to two additional coding passes. (1) Ref0 is 0, ref1 is 0 with a -1 offset, (1) Ref0 is 0 with a -1 offset, ref1 is 0
    WPMCPrecFullRef          =  0     # Increases the number of references in the reference picture lists to account
                                    # for the lost reference slot when reordering is used during a coding pass in WPMCPrecision for reference replication.
                                    # The number of references in non-reordered passes stays unchanged
    WPMCPrecBSlice           =  1     # 2: Apply rounding on every B slice. This efectively disables the evaluation of alternative QPs during RDPictureDecision.
                                    # 1: Disable rounding for non-reference B slices. Non-reference B slices are evaluated for alternative QPs during RDPictureDecision.
                                    # 0: Disable rounding for B slices.

    ##########################################################################################
    # Picture based Multi-pass encoding
    #########################################################################################

    RDPictureDecision        =  0     # Perform multiple pass coding and make RD optimal decision among them
    RDPSliceBTest            =  0     # Perform Slice level RD decision between P and B slices. 
    RDPSliceITest            =  1     # Perform Slice level RD decision between P and I slices. Default value is 1 (enabled).
    RDPictureMaxPassISlice   =  1     # Max number of coding passes for I slices, valid values [1,3], default is 1 
    RDPictureMaxPassPSlice   =  2     # Max number of coding passes for P slices, valid values [1,6], default is 2
    RDPictureMaxPassBSlice   =  3     # Max number of coding passes for B slices, valid values [1,6], default is 3
    RDPictureFrameQPPSlice   =  0     # Perform additional frame level QP check (QP+/-1) for P slices, 0: disabled (default), 1: enabled
    RDPictureFrameQPBSlice   =  0     # Perform additional frame level QP check (QP+/-1) for B slices, 0: disabled, 1: enabled (default)
    RDPictureDeblocking      =  0     # Perform another coding pass to check non-deblocked picture, 0: disabled (default), 1: enabled
    RDPictureDirectMode      =  0     # Perform another coding pass to check the alternative direct mode for B slices, , 0: disabled (default), 1: enabled

    ##########################################################################################
    # Deblocking filter parameters
    ##########################################################################################

    DFParametersFlag         = 0      # Configure deblocking filter (0=parameters below ignored, 1=parameters sent)
                                    # Note that for pictures with multiple slice types, 
                                    # only the type of the first slice will be considered.
    DFDisableRefISlice       = 0      # Disable deblocking filter in reference I coded pictures (0=Filter, 1=No Filter). 
    DFAlphaRefISlice         = 0      # Reference I coded pictures Alpha offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFBetaRefISlice          = 0      # Reference I coded pictures Beta offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFDisableNRefISlice      = 0      # Disable deblocking filter in non reference I coded pictures (0=Filter, 1=No Filter). 
    DFAlphaNRefISlice        = 0      # Non Reference I coded pictures Alpha offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFBetaNRefISlice         = 0      # Non Reference I coded pictures Beta offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFDisableRefPSlice       = 0      # Disable deblocking filter in reference P coded pictures (0=Filter, 1=No Filter). 
    DFAlphaRefPSlice         = 0      # Reference P coded pictures Alpha offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFBetaRefPSlice          = 0      # Reference P coded pictures Beta offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFDisableNRefPSlice      = 0      # Disable deblocking filter in non reference P coded pictures (0=Filter, 1=No Filter). 
    DFAlphaNRefPSlice        = 0      # Non Reference P coded pictures Alpha offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFBetaNRefPSlice         = 0      # Non Reference P coded pictures Beta offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFDisableRefBSlice       = 0      # Disable deblocking filter in reference B coded pictures (0=Filter, 1=No Filter). 
    DFAlphaRefBSlice         = 0      # Reference B coded pictures Alpha offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFBetaRefBSlice          = 0      # Reference B coded pictures Beta offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFDisableNRefBSlice      = 0      # Disable deblocking filter in non reference B coded pictures (0=Filter, 1=No Filter). 
    DFAlphaNRefBSlice        = 0      # Non Reference B coded pictures Alpha offset div. 2, {-6, -5, ... 0, +1, .. +6}
    DFBetaNRefBSlice         = 0      # Non Reference B coded pictures Beta offset div. 2, {-6, -5, ... 0, +1, .. +6}

    ##########################################################################################
    # Error Resilience / Slices
    ##########################################################################################

    SliceMode             =  0   # Slice mode (0=off 1=fixed #mb in slice 2=fixed #bytes in slice 3=use callback)
    SliceArgument         = 50   # Slice argument (Arguments to modes 1 and 2 above)

    num_slice_groups_minus1 = 0  # Number of Slice Groups Minus 1, 0 == no FMO, 1 == two slice groups, etc.
    slice_group_map_type    = 0  # 0:  Interleave, 1: Dispersed,    2: Foreground with left-over,
                                # 3:  Box-out,    4: Raster Scan   5: Wipe
                                # 6:  Explicit, slice_group_id read from SliceGroupConfigFileName
    slice_group_change_direction_flag = 0    # 0: box-out clockwise, raster scan or wipe right,
                                            # 1: box-out counter clockwise, reverse raster scan or wipe left
    slice_group_change_rate_minus1    = 85   #
    SliceGroupConfigFileName          = "sg0conf.cfg"   # Used for slice_group_map_type 0, 2, 6

    UseRedundantPicture   = 0    # 0: not used, 1: enabled
    NumRedundantHierarchy = 1    # 0-4
    PrimaryGOPLength      = 10   # GOP length for redundant allocation (1-16)
                                # NumberReferenceFrames must be no less than PrimaryGOPLength when redundant slice enabled
    NumRefPrimary         = 1    # Actually used number of references for primary slices (1-16)

    ##########################################################################################
    # Search Range Restriction / RD Optimization
    ##########################################################################################

    RestrictSearchRange    =  2  # restriction for (0: blocks and ref, 1: ref, 2: no restrictions)
    RDOptimization         =  1  # rd-optimized mode decision
                                # 0: RD-off (Low complexity mode)
                                # 1: RD-on (High complexity mode)
                                # 2: RD-on (Fast high complexity mode - not work in FREX Profiles)
                                # 3: with losses
                                # 4: RD-on (High complexity mode) with negative skip bias
    I16RDOpt               =  1  # perform rd-optimized mode decision for Intra 16x16 MB
                                # 0: SAD-based mode decision for Intra 16x16 MB
                                # 1: RD-based mode decision for Intra 16x16 MB                        
    SubMBCodingState       =  1  # submacroblock coding state
                                # 0: lowest complexity, do not store or reset coding state during sub-MB mode decision
                                # 1: medium complexity, reset to master coding state (for current mode) during sub-MB mode decision
                                # 2: highest complexity, store and reset coding state during sub-MB mode decision
    DistortionSSIM         =  0  # Compute SSIM distortion. (0: disabled/default, 1: enabled)
    DistortionMS_SSIM      =  0  # Compute Multiscale SSIM distortion. (0: disabled/default, 1: enabled)
    SSIMOverlapSize        =  8  # Overlap size to calculate SSIM distortion (1: pixel by pixel, 8: no overlap)
    DistortionYUVtoRGB     =  0  # Calculate distortion in RGB domain after conversion from YCbCr (0:off, 1:on)
    CtxAdptLagrangeMult    =  0  # Context Adaptive Lagrange Multiplier
                                # 0: disabled (default)
                                # 1: enabled (works best when RDOptimization=0)
    FastCrIntraDecision    =  1  # Fast Chroma intra mode decision (0:off, 1:on)
    DisableThresholding    =  1  # Disable Thresholding of Transform Coefficients (0:off, 1:on)
    DisableBSkipRDO        =  0  # Disable B Skip Mode consideration from RDO Mode decision (0:off, 1:on)
    BiasSkipRDO            =  0  # Negative Bias for Skip/DirectSkip modes (0: off, 1: on)
    ForceTrueRateRDO       =  0  # Force true rate (even zero values) during RDO process
    SkipIntraInInterSlices =  0  # Skips Intra mode checking in inter slices if certain mode decisions are satisfied (0: off, 1: on)
    PSliceSkipDecisionMethod  =  0  # Enable/Control consideration of Skip mode in P slices based on the characteristics of inter modes.
                                # Used in combination with RDOptimization = 4.
                                # 0: Enable always
                                # 1: Enable only when best mode is 16x16 with skip motion vectors and no residual (natural mode)
                                # 2: Enable only when best mode is 16x16 with skip motion vectors
                                # 3: Enable only when best mode is 16x16 and mvs are close to skip motion vectors (+-8)
                                # 4: Enable only when best mode is inter with no residual
                                # 5: Enable only when best mode is inter with no residual or 16x16 with mvs close to skip (+-8)

    WeightY                =  1  # Luma weight for RDO
    WeightCb               =  1  # Cb weight for RDO
    WeightCr               =  1  # Cr weight for RDO

    ##########################################################################################
    # Explicit Lambda Usage
    ##########################################################################################
    UseExplicitLambdaParams  =  0    # Use explicit lambda scaling parameters (0:disabled, 1:enable lambda weight, 2: use explicit lambda value)
    DisableDistanceLambdaScale = 0   # Disable Distance based lambda scaling
    UpdateLambdaChromaME     =  0    # Update lambda given Chroma ME consideration
    FixedLambdaISlice        =  0.1  # Fixed Lambda value for I slices
    FixedLambdaPSlice        =  0.1  # Fixed Lambda value for P slices
    FixedLambdaBSlice        =  0.1  # Fixed Lambda value for B slices
    FixedLambdaRefBSlice     =  0.1  # Fixed Lambda value for Referenced B slices
    FixedLambdaSPSlice       =  0.1  # Fixed Lambda value for SP slices
    FixedLambdaSISlice       =  0.1  # Fixed Lambda value for SI slices

    LambdaWeightISlice       =  0.65 # scaling param for I slices. This will be used as a multiplier i.e. lambda=LambdaWeightISlice * 2^((QP-12)/3)
    LambdaWeightPSlice       =  0.68 # scaling param for P slices. This will be used as a multiplier i.e. lambda=LambdaWeightPSlice * 2^((QP-12)/3)
    LambdaWeightBSlice       =  0.68 # scaling param for B slices. This will be used as a multiplier i.e. lambda=LambdaWeightBSlice * 2^((QP-12)/3)
    LambdaWeightRefBSlice    =  0.68 # scaling param for Referenced B slices. This will be used as a multiplier i.e. lambda=LambdaWeightRefBSlice * 2^((QP-12)/3)
    LambdaWeightSPSlice      =  0.68 # scaling param for SP slices. This will be used as a multiplier i.e. lambda=LambdaWeightSPSlice * 2^((QP-12)/3)
    LambdaWeightSISlice      =  0.65 # scaling param for SI slices. This will be used as a multiplier i.e. lambda=LambdaWeightSISlice * 2^((QP-12)/3)

    LossRateA                =  5  # expected packet loss rate of the channel for the first partition, only valid if RDOptimization = 3
    LossRateB                =  0  # expected packet loss rate of the channel for the second partition, only valid if RDOptimization = 3
    LossRateC                =  0  # expected packet loss rate of the channel for the third partition, only valid if RDOptimization = 3
    FirstFrameCorrect        =  0  # If 1, the first frame is encoded under the assumption that it is always correctly received. 
    NumberOfDecoders         = 30  # Numbers of decoders used to simulate the channel, only valid if RDOptimization = 3
    RestrictRefFrames        =  0  # Doesnt allow reference to areas that have been intra updated in a later frame.

    ##########################################################################################
    # Additional Stuff
    #########################################################################################

    UseConstrainedIntraPred  =  0  # If 1, Inter pixels are not used for Intra macroblock prediction.

    NumberofLeakyBuckets     =  8                      # Number of Leaky Bucket values
    LeakyBucketRateFile      =  "leakybucketrate.cfg"  # File from which encoder derives rate values
    LeakyBucketParamFile     =  "leakybucketparam.cfg" # File where encoder stores leakybucketparams

    NumFramesInELayerSubSeq  = 0  # number of frames in the Enhanced Scalability Layer(0: no Enhanced Layer)

    SparePictureOption        =  0   # (0: no spare picture info, 1: spare picture available)
    SparePictureDetectionThr  =  6   # Threshold for spare reference pictures detection
    SparePicturePercentageThr = 92   # Threshold for the spare macroblock percentage

    PicOrderCntType           = 0    # (0: POC mode 0, 1: POC mode 1, 2: POC mode 2)

    ########################################################################################
    #Rate control
    ########################################################################################

    RateControlEnable       = 1     # 0 Disable, 1 Enable
    '''
    file.write(cfg5)

    file.write('Bitrate                 = ' + bitrate + ' # Bitrate(bps)\n')

    cfg6 = '''
    InitialQP               = 32    # Initial Quantization Parameter for the first I frame
                                    # InitialQp depends on two values: Bits Per Picture,
                                    # and the GOP length
    BasicUnit               = 0     # Number of MBs in the basic unit
                                    # should be a fraction of the total number
                                    # of MBs in a frame ("0" sets a BU equal to a frame)
    ChannelType             = 0     # type of channel( 1=time varying channel; 0=Constant channel)
    RCUpdateMode            = 2     # Rate Control type. Modes supported :
                                    # 0 = original JM rate control,
                                    # 1 = rate control that is applied to all frames regardless of the slice type,
                                    # 2 = original plus intelligent QP selection for I and B slices (including Hierarchical),
                                    # 3 = original + hybrid quadratic rate control for I and B slice using bit rate statistics
                                    #
    RCISliceBitRatio        = 1.0   # target ratio of bits for I-coded pictures compared to P-coded Pictures (for RCUpdateMode=3)
    RCBSliceBitRatio0       = 0.5   # target ratio of bits for B-coded pictures compared to P-coded Pictures - temporal level 0 (for RCUpdateMode=3)
    RCBSliceBitRatio1       = 0.25  # target ratio of bits for B-coded pictures compared to P-coded Pictures - temporal level 1 (for RCUpdateMode=3)
    RCBSliceBitRatio2       = 0.25  # target ratio of bits for B-coded pictures compared to P-coded Pictures - temporal level 2 (for RCUpdateMode=3)
    RCBSliceBitRatio3       = 0.25  # target ratio of bits for B-coded pictures compared to P-coded Pictures - temporal level 3 (for RCUpdateMode=3)
    RCBSliceBitRatio4       = 0.25  # target ratio of bits for B-coded pictures compared to P-coded Pictures - temporal level 4 (for RCUpdateMode=3)
    RCBoverPRatio           = 0.45  # ratio of bit rate usage of a B-coded picture over a P-coded picture for the SAME QP (for RCUpdateMode=3)
    RCIoverPRatio           = 3.80  # ratio of bit rate usage of an I-coded picture over a P-coded picture for the SAME QP (for RCUpdateMode=3)
    RCMinQPPSlice           =  8    # minimum P Slice QP value for rate control
    RCMaxQPPSlice           = 42    # maximum P Slice QP value for rate control
    RCMinQPBSlice           =  8    # minimum B Slice QP value for rate control
    RCMaxQPBSlice           = 42    # maximum B Slice QP value for rate control
    RCMinQPISlice           =  8    # minimum I Slice QP value for rate control
    RCMaxQPISlice           = 42    # maximum I Slice QP value for rate control
    RCMinQPSPSlice          =  8    # minimum SP Slice QP value for rate control
    RCMaxQPSPSlice          = 40    # maximum SP Slice QP value for rate control
    RCMinQPSISlice          =  8    # minimum SI Slice QP value for rate control
    RCMaxQPSISlice          = 42    # maximum SI Slice QP value for rate control
    RCMaxQPChange           =  4    # maximum QP change for frames of the base layer

    ########################################################################################
    #Fast Mode Decision
    ########################################################################################
    EarlySkipEnable         = 0     # Early skip detection (0: Disable 1: Enable)
    SelectiveIntraEnable    = 0     # Selective Intra mode decision (0: Disable 1: Enable)

    ########################################################################################
    #FREXT stuff
    ########################################################################################

    YUVFormat               = 1     # YUV format (0=4:0:0, 1=4:2:0, 2=4:2:2, 3=4:4:4)
    RGBInput                = 0     # 1=RGB input, 0=GBR or YUV input
    SeparateColourPlane     = 0     # 4:4:4 coding: 0=Common mode, 1=Independent mode
    SourceBitDepthLuma      = 8     # Source Bit Depth for Luma color component (8...14 bits)
    SourceBitDepthChroma    = 8     # Source Bit Depth for Chroma color components (8...14 bits)
    SourceBitDepthRescale   = 0     # Rescale bit depth of source for output (0: Disable 1: Enable)
    OutputBitDepthLuma      = 8     # Output Bit Depth for Luma color component (8...14 bits)
    OutputBitDepthChroma    = 8     # Output Bit Depth for Chroma color components (8...14 bits)

    CbQPOffset              = 0     # Chroma QP offset for Cb-part (-51..51)
    CrQPOffset              = 0     # Chroma QP offset for Cr-part (-51..51)
    Transform8x8Mode        = 1     # (0: only 4x4 transform, 1: allow using 8x8 transform additionally, 2: only 8x8 transform)
    ReportFrameStats        = 0     # (0:Disable Frame Statistics 1: Enable)
    DisplayEncParams        = 0     # (0:Disable Display of Encoder Params 1: Enable)
    Verbose                 = 1     # level of display verboseness 
                                    # 0: short, 1: normal (default), 2: detailed, 3: detailed/nvb
    SkipGlobalStats         = 0     # Disable global stat accumulation  (Set to 1 to avoid bipred core dump)

    ########################################################################################
    #Q-Matrix (FREXT)
    ########################################################################################
    QmatrixFile              = "q_matrix.cfg"

    ScalingMatrixPresentFlag = 0    # Enable Q_Matrix  (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag0  = 3    # Intra4x4_Luma    (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag1  = 3    # Intra4x4_ChromaU (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag2  = 3    # Intra4x4_chromaV (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag3  = 3    # Inter4x4_Luma    (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag4  = 3    # Inter4x4_ChromaU (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag5  = 3    # Inter4x4_ChromaV (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag6  = 3    # Intra8x8_Luma    (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag7  = 3    # Inter8x8_Luma    (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag8  = 3    # Intra8x8_ChromaU for 4:4:4 (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag9  = 3    # Inter8x8_ChromaU for 4:4:4 (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag10 = 3    # Intra8x8_ChromaV for 4:4:4 (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)
    ScalingListPresentFlag11 = 3    # Inter8x8_ChromaV for 4:4:4 (0 Not present, 1 Present in SPS, 2 Present in PPS, 3 Present in both SPS & PPS)

    ########################################################################################
    #Rounding Offset control
    ########################################################################################

    OffsetMatrixPresentFlag  = 0    # Enable Explicit Offset Quantization Matrices  (0: disable 1: enable)
    QOffsetMatrixFile        = "q_offset.cfg" # Explicit Quantization Matrices file
    OffsetMatrixFlat         = 0    # 0: use default initialization offsets (1/3 intra, 1/6 inter)
                                    # 1: offsets initialized to 0.5
                                    # 2: offsets initialized to 0.5 for chroma intra, otherwise uses default values

    AdaptiveRounding         = 1    # Enable Adaptive Rounding based on JVT-N011 (0: disable, 1: enable)
    AdaptRoundingFixed       = 0    # Enable Global Adaptive rounding for all qps (0: disable, 1: enable - default/old)
    AdaptRndPeriod           = 16   # Period in terms of MBs for updating rounding offsets. 
                                    # 0 performs update at the picture level. Default is 16. 1 is as in JVT-N011.
    AdaptRndChroma           = 1    # Enables coefficient rounding adaptation for chroma

    AdaptRndWFactorIRef      = 8    # Adaptive Rounding Weight for I/SI slices in reference pictures /4096
    AdaptRndWFactorPRef      = 8    # Adaptive Rounding Weight for P/SP slices in reference pictures /4096
    AdaptRndWFactorBRef      = 8    # Adaptive Rounding Weight for B slices in reference pictures /4096
    AdaptRndWFactorINRef     = 8    # Adaptive Rounding Weight for I/SI slices in non reference pictures /4096
    AdaptRndWFactorPNRef     = 8    # Adaptive Rounding Weight for P/SP slices in non reference pictures /4096
    AdaptRndWFactorBNRef     = 8    # Adaptive Rounding Weight for B slices in non reference pictures /4096

    AdaptRndCrWFactorIRef    = 8    # Chroma Adaptive Rounding Weight for I/SI slices in reference pictures /4096
    AdaptRndCrWFactorPRef    = 8    # Chroma Adaptive Rounding Weight for P/SP slices in reference pictures /4096
    AdaptRndCrWFactorBRef    = 8    # Chroma Adaptive Rounding Weight for B slices in reference pictures /4096
    AdaptRndCrWFactorINRef   = 8    # Chroma Adaptive Rounding Weight for I/SI slices in non reference pictures /4096
    AdaptRndCrWFactorPNRef   = 8    # Chroma Adaptive Rounding Weight for P/SP slices in non reference pictures /4096
    AdaptRndCrWFactorBNRef   = 8    # Chroma Adaptive Rounding Weight for B slices in non reference pictures /4096

    ################################################################
    # Rate Distortion Optimized Quantization
    ################################################################
    UseRDOQuant              =  0 # Use Rate Distortion Optimized Quantization (0=disable, 1=enable)
    RDOQ_DC                  =  1 # Enable Rate Distortion Optimized Quantization for DC components (0=disable, 1=enable)
    RDOQ_CR                  =  1 # Enable Rate Distortion Optimized Quantization for Chroma components (0=disable, 1=enable)
    RDOQ_DC_CR               =  1 # Enable Rate Distortion Optimized Quantization for Chroma DC components (0=disable, 1=enable)
    RDOQ_QP_Num              =  5 # 1-9: Number of QP tested in RDO_Q (I/P/B slice)
    RDOQ_CP_Mode             =  0 # copy Mode from first QP tested
    RDOQ_CP_MV               =  0 # copy MV from first QP tested
    RDOQ_Fast                =  0 # Fast RDOQ decision method for multiple QPs

    ########################################################################################
    #Lossless Coding (FREXT)
    ########################################################################################

    LosslessCoding           = 0    # Enable lossless coding when qpprime_y is zero (0 Disabled, 1 Enabled)

    ########################################################################################
    #Fast Motion Estimation Control Parameters
    ########################################################################################

    SearchMode               = 3    # Motion estimation mode
                                    # -1 = Full Search
                                    #  0 = Fast Full Search (default)
                                    #  1 = UMHexagon Search
                                    #  2 = Simplified UMHexagon Search
                                    #  3 = Enhanced Predictive Zonal Search (EPZS)
                                    
    UMHexDSR                 = 1    # Use Search Range Prediction. Only for UMHexagonS method
                                    # (0:disable, 1:enabled/default)
    UMHexScale               = 3    # Use Scale_factor for different image sizes. Only for UMHexagonS method
                                    # (0:disable, 3:/default)
                                    # Increasing value can speed up Motion Search.

    EPZSPattern              = 2    # Select EPZS primary refinement pattern.
                                    # (0: small diamond, 1: square, 2: extended diamond/default,
                                    # 3: large diamond, 4: SBP Large Diamond,
                                    # 5: PMVFAST )
    EPZSDualRefinement       = 3    # Enables secondary refinement pattern.
                                    # (0:disabled, 1: small diamond, 2: square,
                                    # 3: extended diamond/default, 4: large diamond,
                                    # 5: SBP Large Diamond, 6: PMVFAST )
    EPZSFixedPredictors      = 3    # Enables Window based predictors
                                    # (0:disabled, 1: P only, 2: P and B, 3: Pic Boundary + P and B/default)
    EPZSAggressiveWindow     = 0    # Use Aggressive Window pattern for EPZS (0: disabled, 1: enabled)
    EPZSTemporal             = 1    # Enables temporal predictors
                                    # (0: disabled, 1: enabled/default)
    EPZSSpatialMem           = 1    # Enables spatial memory predictors
                                    # (0: disabled, 1: enabled/default)
    EPZSBlockType            = 1    # Enables block type Predictors
                                    # (0: disabled, 1: enabled/default)
    EPZSMinThresScale        = 0    # Scaler for EPZS minimum threshold (0 default).
                                    # Increasing value can speed up encoding.
    EPZSMedThresScale        = 1    # Scaler for EPZS median threshold (1 default).
                                    # Increasing value can speed up encoding.
    EPZSMaxThresScale        = 2    # Scaler for EPZS maximum threshold (1 default).
                                    # Increasing value can speed up encoding.
    EPZSSubPelME             = 1    # EPZS Subpel ME consideration
    EPZSSubPelMEBiPred       = 1    # EPZS Subpel ME consideration for BiPred partitions
    EPZSSubPelThresScale     = 1    # EPZS Subpel ME Threshold scaler
    EPZSSubPelGrid           = 1    # Perform EPZS using a subpixel grid
    HMEEnable                = 1    # Enable Hierarchical Motion Estimation consideration with EPZS (does not work with other ME Engines)
    EPZSUseHMEPredictors     = 1    # Use HME motion vectors during EPZS refinement
    UseDistortionReorder     = 1    # Use Distortion based reordering. If HME is enabled, then HME results are used, otherwise zero motion distortion is computed.

    ########################################################################################
    # SEI Parameters
    ########################################################################################

    ToneMappingSEIPresentFlag = 0    # Enable Tone mapping SEI  (0 Not present, 1 Present)
    ToneMappingFile           = "ToneMapping.cfg"

    GenerateSEIMessage        = 0                    # Generate an SEI Text Message
    SEIMessageText            = "H.264/AVC Encoder"  # Text SEI Message

    SEIFPAType            = -1     # Set frame packing arrangement type
                                # -1 = disabled
                                #  0 = checkerboard
                                #  1 = columns alternate
                                #  2 = lines alternate
                                #  3 = side by side
                                #  4 = top and bottom
                                #  5 = frame alternate
                                #  6 = 2D
                                #  7 = tile

    UseMVLimits               = 0                    # Use MV Limits
    SetMVXLimit               = 512                  # Horizontal MV Limit (in integer units)
    SetMVYLimit               = 512                  # Vertical MV Limit (in integer units)

    ########################################################################################
    # VUI Parameters
    ########################################################################################
    # the variables below do not affect encoding and decoding
    # (many are dummy variables but others can be useful when supported by the decoder)

    EnableVUISupport                                = 0      # Enable VUI Parameters

    # display parameters
    VUI_aspect_ratio_info_present_flag              = 0
    VUI_aspect_ratio_idc                            = 1
    VUI_sar_width                                   = 0
    VUI_sar_height                                  = 0
    VUI_overscan_info_present_flag                  = 0
    VUI_overscan_appropriate_flag                   = 0
    VUI_video_signal_type_present_flag              = 0
    VUI_video_format                                = 5
    VUI_video_full_range_flag                       = 0
    VUI_colour_description_present_flag             = 0
    VUI_colour_primaries                            = 2
    VUI_transfer_characteristics                    = 2
    VUI_matrix_coefficients                         = 2
    VUI_chroma_location_info_present_flag           = 0
    VUI_chroma_sample_loc_type_top_field            = 0
    VUI_chroma_sample_loc_type_bottom_field         = 0
    VUI_timing_info_present_flag                    = 0
    VUI_num_units_in_tick                           = 1000
    VUI_time_scale                                  = 60000
    VUI_fixed_frame_rate_flag                       = 0

    # nal hrd parameters
    VUI_nal_hrd_parameters_present_flag             = 0
    VUI_nal_cpb_cnt_minus1                          = 0
    VUI_nal_bit_rate_scale                          = 0
    VUI_nal_cpb_size_scale                          = 0
    VUI_nal_bit_rate_value_minus1                   = 0
    VUI_nal_cpb_size_value_minus1                   = 0
    VUI_nal_vbr_cbr_flag                            = 0
    VUI_nal_initial_cpb_removal_delay_length_minus1 = 23
    VUI_nal_cpb_removal_delay_length_minus1         = 23
    VUI_nal_dpb_output_delay_length_minus1          = 23
    VUI_nal_time_offset_length                      = 24

    # vlc hrd parameters
    VUI_vcl_hrd_parameters_present_flag             = 0
    VUI_vcl_cpb_cnt_minus1                          = 0
    VUI_vcl_bit_rate_scale                          = 0
    VUI_vcl_cpb_size_scale                          = 0
    VUI_vcl_bit_rate_value_minus1                   = 0
    VUI_vcl_cpb_size_value_minus1                   = 0
    VUI_vcl_vbr_cbr_flag                            = 0
    VUI_vcl_initial_cpb_removal_delay_length_minus1 = 23
    VUI_vcl_cpb_removal_delay_length_minus1         = 23
    VUI_vcl_dpb_output_delay_length_minus1          = 23
    VUI_vcl_time_offset_length                      = 24
    VUI_low_delay_hrd_flag                          = 0

    # other parameters (i.e. bitsream restrictions)
    VUI_pic_struct_present_flag                     = 0
    VUI_bitstream_restriction_flag                  = 0
    VUI_motion_vectors_over_pic_boundaries_flag     = 1
    VUI_max_bytes_per_pic_denom                     = 0
    VUI_max_bits_per_mb_denom                       = 0
    VUI_log2_max_mv_length_vertical                 = 16
    VUI_log2_max_mv_length_horizontal               = 16
    VUI_num_reorder_frames                          = 16
    VUI_max_dec_frame_buffering                     = 16

    '''
    file.write(cfg6)
    file.close()

    # fileName2 = rawNameSplit[0] + '.sh'
    # file2 = open(fileName2, mode='a', encoding='utf-8')
    # file2.write('./lencod.exe -f ' + fileName + '\n')
    # file2.close()
    # os.system('chmod 777 ' + fileName2)
    # return fileName2


bitrateList   = ['700', '1000', '2000', '3000', '4000', '6000', '8000', '10000']  # --bitrate <integer>     Set bitrate (kbit/s)
rawName       = input('Raw video name:   ')
rawFrames     = input('Raw video frames: ')
rawNameSplit  = rawName.split('.')           #Result: ['apple_tree_1920x1080_30', 'yuv']
shellFileName = rawNameSplit[0] + '.sh'      #Result:  'apple_tree_1920x1080_30.sh'
shellFile     = open(shellFileName, mode='w', encoding='utf-8')
shellFile.write('mkdir /data/WispChan/jm_benchmark_output/' + rawNameSplit[0] + '\n')
for b in bitrateList:
    generate(b, rawName, rawFrames)
    shellFile.write('./lencod.exe -f ' + rawNameSplit[0] + '_' + b + '.cfg')
    if b!='10000':
        shellFile.write(' && ')
shellFile.close()
os.system('chmod 777 ' + shellFileName)

# sequences = ['apple_tree_1920x1080_30.yuv', 'asteroid_landing_1920x1080_25.yuv', "baseball_1920x1080_60.yuv", "boat_1920x1080_60.yuv", "boring_concert_1920x1080_30.yuv", "carpets_1920x1080_25.yuv", "cgi_cricket_1920x1080_25.yuv", "chili_pepper_1920x1080_60.yuv", "christmas_cats_1920x1080_25.yuv", "city_1920x1080_25.yuv",
#             "crowd_run_1920x1080_50.yuv", "diy_mixer_1920x1080_25.yuv", "epic_clip_1920x1080_24.yuv", "fifa_1920x1080_52.yuv", "fishing_1920x1080_25.yuv", "forest_eye_1920x1080_25.yuv", "graycolor_concert_1920x1080_24.yuv", "green_grass_1920x1080_30.yuv", "hard_rock_1920x1080_25.yuv", "keeping_warm_1920x1080_30.yuv", 
#             "kids_1920x1080_30.yuv", "lecture_1440x1080_25.yuv", "lemonade_ads_1920x1080_25.yuv", "mobile_1920x1080_24.yuv", "mordor_gameplay_1920x1080_39.yuv", "mosquito_1920x1080_30.yuv", "mosquito_movie_1920x1080_24.yuv", "motobike_1920x1080_24.yuv", "motofootball_1920x1080_50.yuv", "mountains_1920x1080_30.yuv", 
#             "new_york_1920x1080_24.yuv", "nfl_1920x1080_30.yuv", "night_concert_1440x1080_30.yuv", "night_sky_1920x1080_24.yuv", "night_walk_1920x1080_24.yuv", "old_ship_1920x1080_60.yuv", "orchestra_1920x1080_25.yuv", "painting_slideshow_1920x1080_30.yuv", "photo_art_1920x1080_24.yuv", "road_timelapse_1920x1080_30.yuv",
#             "roller_girl_1920x1080_24.yuv", "seawave_1920x1080_24.yuv", "shakerwalk_1920x1080_25.yuv", "sheriff_1920x1080_30.yuv", "skiing_1920x1080_25.yuv", "strange_clip_1920x1080_25.yuv", "street_report_1920x1080_60.yuv", "street_views_1920x1080_25.yuv", "townday_1920x1080_30.yuv", "tractor_1920x1080_25.yuv", "water_flow_1920x1080_24.yuv"]
